# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysenec']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

entry_points = \
{'console_scripts': ['senec = pysenec.cli:main']}

setup_kwargs = {
    'name': 'pysenec',
    'version': '0.2.0',
    'description': 'Unofficial, local SENEC Battery Client',
    'long_description': None,
    'author': 'Mikołaj Chwalisz',
    'author_email': 'm.chwalisz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
