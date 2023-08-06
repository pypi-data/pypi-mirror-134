# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mixologist']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-mqtt>=0.11.0,<0.12.0',
 'fastapi>=0.70.1,<0.71.0',
 'httpx>=0.21.1,<0.22.0',
 'uvicorn>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'mixologist',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'David Francos',
    'author_email': 'opensource@davidfrancos.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
