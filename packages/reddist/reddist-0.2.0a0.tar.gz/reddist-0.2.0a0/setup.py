# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reddist', 'reddist.cachers', 'reddist.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles==0.6.0', 'aioredis>=2.0.1,<3.0.0', 'asyncpraw>=7.5.0,<8.0.0']

setup_kwargs = {
    'name': 'reddist',
    'version': '0.2.0a0',
    'description': 'Just a simple library for caching reddit posts',
    'long_description': None,
    'author': 'CaffieneDuck',
    'author_email': 'samrid.pandit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
