# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yh_poetry']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'yh-poetry',
    'version': '2.0.0',
    'description': '',
    'long_description': None,
    'author': 'sutianru',
    'author_email': 'sutianru@amazon.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
