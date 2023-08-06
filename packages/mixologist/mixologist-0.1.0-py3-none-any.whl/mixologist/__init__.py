"""Mixology.

Automatic cocktail alcohol dispenser.

Configure MQTT on two tasmota-enabled relay devices.
Set them up in main.ini as per the example
"""

import asyncio
import configparser
import functools
import json
import operator
import os
from contextlib import suppress
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from typing import List
from asyncio_mqtt import Client

from fastapi import FastAPI, Query, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE = os.getenv('BASE_URL', '')
RPRE = {'prefix': BASE} if os.getenv('BASE_URL') else {}
print(f"Starting with parameters {RPRE}")
router = APIRouter(**RPRE)

app = FastAPI()
app.mount(f"{BASE}/js", StaticFiles(directory="ui/dist/js/"), name="js")
app.mount(f"{BASE}/css", StaticFiles(directory="ui/dist/css/"), name="css")
app.mount(f"{BASE}/images", StaticFiles(directory="ui/images"), name="images")


class TasmotaFinder:
    def __init__(self):
        self.tasmotas = []
        self.config = configparser.ConfigParser()
        self.config.read('main.ini')
        self.url = self.config['main'].get('url')

    def save_config(self):
        self.config.write(open('main.ini', 'w'))

    @property
    def tasmotas_with_config(self):
        result = defaultdict(dict)
        for tasmota in self.tasmotas:
            active = False
            if tasmota['topic'] in self.config.sections():
                for key, values in self.config[tasmota['topic']].items():
                    result[tasmota['topic']][key] = values.split(',') + [True]
                    active = True
            if not active:
                for key in tasmota['relays']:
                    result[tasmota['topic']][key] = [None, None, None]
        return {"url": self.config["main"]['url'], 'tasmotas': result}

    def reload_config(self):
        self.config.read('main.ini')
        return {"status": True}

    async def retry_main(self):
        while True:
            with suppress(Exception):
                await self.run_main()
                await asyncio.sleep(5)

    async def run_main(self):
        async with Client(self.url) as client:
            btop = "tasmota/discovery/+/config"
            async with client.filtered_messages(btop) as messages:
                await client.subscribe("tasmota/discovery/#")
                async for message in messages:
                    loaded = json.loads(message.payload)
                    if any(loaded['rl']):
                        relays = [a for a, b in enumerate(loaded['rl']) if b]
                        self.tasmotas.append({
                            'topic': loaded['t'],
                            'ip': loaded['ip'],
                            'relays': relays
                        })

    async def dispense(self, alcohol, quantity, client):
        def get_data(tasmotas):
            for topic, tasmota in tasmotas['tasmotas'].items():
                for relay, values in tasmota.items():
                    if not values:
                        continue
                    alcohol_, time_per_cl, enabled = values
                    if not enabled:
                        continue
                    if alcohol_ == alcohol:
                        topic = f"cmnd/{topic}/Power{relay}"
                        return topic, time_per_cl

        if values := get_data(self.tasmotas_with_config):
            topic, time_per_cl = values
            print(f"Doing {topic} for {(int(time_per_cl) / 1000) * quantity}s")
            await client.publish(topic, payload=b'ON')
            await asyncio.sleep(int(time_per_cl) / 1000 * quantity)
            await client.publish(topic, payload=b'OFF')
            print(f"Finished doing {topic} for {(int(time_per_cl) / 1000) * quantity}s")
        return {"status": False}


runner = TasmotaFinder()


class Cocktail(dict):
    """Represent a cocktail"""
    def __hash__(self):
        return self['id']

    @property
    def alcohols(self) -> set:
        """Return list of alcohols in ingredients"""
        def is_juice(ing):
            """Avoid non-alcoholic drinks"""
            fsc = ('bitter', 'juice', 'syrup', 'spoon', 'yolk', 'hot',
                   'ginger', 'cachaca', 'milk', 'cola', 'water')
            return any(a in ing.lower() for a in fsc)

        return set(
            filter(lambda x: x,
                   [a if not is_juice(a) else None for a in self.ingredients]))

    @property
    def quantified_alcohols(self) -> set:
        """Return list of alcohols in ingredients"""
        def is_juice(ing):
            """Avoid non-alcoholic drinks"""
            fsc = ('bitter', 'juice', 'syrup', 'spoon', 'yolk', 'hot',
                   'ginger', 'cachaca', 'milk', 'cola', 'water')
            return any(a in ing.lower() for a in fsc)

        ing = [[a, b] if not is_juice(a) else [None, None]
               for a, b in self.quantified_ingredients]
        return set(tuple([tuple([a, b]) for a, b in ing if a]))

    @property
    def quantified_ingredients(self):
        """non-special ingredients, may return '' on special ones."""
        return [[a.get('ingredient', ''),
                 a.get('amount', '')] for a in self['ingredients']]

    @property
    def ingredients(self):
        """non-special ingredients, may return '' on special ones."""
        return [a.get('ingredient', '') for a in self['ingredients']]

    def quantity(self, ingredient_name):
        match = next(
            iter([
                ing for ing in self['ingredients']
                if ing.get('ingredient') == ingredient_name
            ]))
        return match['amount']

    def num_similar(self, other):
        """Return the number of equal alcohols in both beverages"""
        return len(self.alcohols & other.alcohols)


COCKTAILS = [
    Cocktail(b | dict(id=a))
    for a, b in enumerate(json.load(open('recipes.json')))
]


@lru_cache
def sorted_recipes(curr):
    """Sort recipes.

    Given a set of base ingredients, get the most recipes we can achieve by
    buying the less ingredients
    """
    curr = set(curr)

    similarity = {}
    for p1, p2 in combinations(COCKTAILS, 2):
        similarity.setdefault((p1, p2), p1.num_similar(p2))
    similarity = sorted(similarity, key=lambda x: similarity[x], reverse=True)
    sorted_ids = []
    for (left, right) in similarity:
        if left not in sorted_ids:
            sorted_ids.append(left)
        elif right not in sorted_ids:
            sorted_ids.append(right)

    return [a for a in sorted_ids if not a.alcohols - curr]


@router.get("/", response_class=HTMLResponse)
async def index():
    return Path('ui/dist/index.html').read_text()


@router.get("/recipes/")
async def calculate_recipes(current: List[str] = Query(None)):
    """Return recipes given a list of available alcohols"""
    if not current:
        return []
    return sorted_recipes(tuple(current))


@router.post("/recipes/")
async def do_recipe(request: Request):
    """Execute a recipe"""
    cocktail = Cocktail(await request.json())
    result = {}
    tasks = []
    async with Client(runner.url) as client:
        for alcohol, quantity in cocktail.quantified_alcohols:
            result[alcohol] = quantity
            tasks.append(runner.dispense(alcohol, quantity, client))
        await asyncio.gather(*tasks)
    return {"status": "OK", "result": result}


@router.get("/alcohols")
async def ingredients():
    """Return all available alcoholic ingredients"""
    return functools.reduce(operator.or_, [a.alcohols for a in COCKTAILS])


@router.get("/settings")
async def tasmotas():
    """Return all discovered tasmotas"""
    return runner.tasmotas_with_config


@router.delete("/settings")
async def update_tasmotas():
    """Update tasmotas"""
    return runner.reload_config()


@router.post("/settings")
async def update_settings(request: Request):
    """Execute a recipe"""
    settings = await request.json()
    runner.config['main']['url'] = settings['url']
    for tasmota, elem in settings['tasmotas'].items():
        if tasmota not in runner.config.sections():
            runner.config.add_section(tasmota)
        for relay, values in elem.items():
            if values[2]:
                runner.config[tasmota][relay] = f"{values[0]},{values[1]}"
            elif relay in runner.config[tasmota]:
                del runner.config[tasmota][relay]
    runner.save_config()
    return runner.reload_config()


@app.on_event('startup')
async def app_startup():
    asyncio.create_task(runner.run_main())

app.include_router(router)
