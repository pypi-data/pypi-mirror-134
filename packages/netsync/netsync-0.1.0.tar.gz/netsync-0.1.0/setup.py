# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netsync']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'netsync',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'A. Naji',
    'author_email': 'asseel.naji96@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
