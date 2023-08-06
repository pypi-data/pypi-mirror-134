# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reloadium']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'reloadium',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Damian Krystkiewicz',
    'author_email': 'damian@reloadware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
