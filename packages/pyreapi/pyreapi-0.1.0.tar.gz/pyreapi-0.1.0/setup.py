# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyreapi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyreapi',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Adam Budziak',
    'author_email': 'adambudziak@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
