# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['serve_me_once']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'serve-me-once',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Peder Bergebakken Sundt',
    'author_email': 'pbsds@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
