# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roxie']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'roxie',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Rerury',
    'author_email': 'rerury.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
