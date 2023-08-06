# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typety']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'typety',
    'version': '1.0.3',
    'description': 'A simple python packages that adds a typing effect to strings',
    'long_description': None,
    'author': 'Dragonlord1005',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Dragonlord1005/typety',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
