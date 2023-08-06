# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['c27cache']

package_data = \
{'': ['*']}

install_requires = \
['pytest-asyncio==0.15.1',
 'python-dateutil>=2.8.2,<3.0.0',
 'pytz>=2021.3,<2022.0',
 'redis>=4.1.0,<5.0.0']

setup_kwargs = {
    'name': 'c27cache',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'SR',
    'author_email': 'sid.ravichandran@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
