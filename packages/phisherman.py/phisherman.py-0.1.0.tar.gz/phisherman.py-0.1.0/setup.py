# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['phisherman']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'mkdocs>=1.2.3,<2.0.0',
 'mkdocstrings>=0.17.0,<0.18.0',
 'pytkdocs[numpy-style]>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'phisherman.py',
    'version': '0.1.0',
    'description': 'Async API Wrapper for Phisherman.gg in Python',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
