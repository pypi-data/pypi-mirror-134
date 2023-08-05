# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meta-weather-cli']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['meta-weather-cli = meta_weather_cli:main']}

setup_kwargs = {
    'name': 'meta-weather-cli',
    'version': '0.1.0',
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
