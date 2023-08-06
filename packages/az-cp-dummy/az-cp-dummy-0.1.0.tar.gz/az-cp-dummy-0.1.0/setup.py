# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['az_cp_dummy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'az-cp-dummy',
    'version': '0.1.0',
    'description': 'A dummy package to test pip & similar',
    'long_description': None,
    'author': 'Francesco Pasa',
    'author_email': 'francesco.pasa@astrazeneca.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
