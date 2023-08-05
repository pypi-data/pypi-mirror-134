# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meta_weather_cli']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['meta-weather-cli = meta_weather_cli:cli']}

setup_kwargs = {
    'name': 'meta-weather-cli',
    'version': '0.1.8',
    'description': 'A CLI to check weather in cities around the globe',
    'long_description': None,
    'author': 'Omer Ben David',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
