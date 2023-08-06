# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['phisherman']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'phisherman.py',
    'version': '0.1.1',
    'description': 'Async API Wrapper for Phisherman.gg in Python',
    'long_description': '# Phisherman.py\n\n\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/QristaLabs/phisherman.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
