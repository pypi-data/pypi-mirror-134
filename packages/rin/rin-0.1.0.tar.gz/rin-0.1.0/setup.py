# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rin', 'rin.gateway', 'rin.models', 'rin.rest', 'rin.types']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'typing-extensions>=4.0.1,<5.0.0']

setup_kwargs = {
    'name': 'rin',
    'version': '0.1.0',
    'description': 'A successor to the Lefi project',
    'long_description': None,
    'author': 'an-dyy',
    'author_email': 'andy.development@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
