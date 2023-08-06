# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['didyou']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'didyou',
    'version': '0.1.0',
    'description': 'Misspelling detection tool',
    'long_description': None,
    'author': 'Gabriel Gazola Milan',
    'author_email': 'gabriel.gazola@poli.ufrj.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
