# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monday_item_parser', 'monday_item_parser.fields']

package_data = \
{'': ['*']}

install_requires = \
['bidict>=0.21.4,<0.22.0', 'monday>=1.2.7,<2.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'monday-item-parser',
    'version': '0.1.2',
    'description': 'monday-item-parser is a library used to define Monday items structure in a specific board, and lets the user fetch, create, update and delete items from this board.',
    'long_description': None,
    'author': 'Aviv Atedgi',
    'author_email': 'aviv.atedgi2000@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
