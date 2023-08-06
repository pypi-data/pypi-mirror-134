# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djognito']

package_data = \
{'': ['*']}

install_requires = \
['Django<=3',
 'djangorestframework>=3.13.1,<4.0.0',
 'python-jose[cryptography]>=3.3.0,<4.0.0']

setup_kwargs = {
    'name': 'djognito',
    'version': '0.1.0',
    'description': 'Auth module for using AWS Cognito with DRF',
    'long_description': '',
    'author': 'Prakash2403',
    'author_email': 'rishurai24@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Prakash2403/Djognito',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.6',
}


setup(**setup_kwargs)
