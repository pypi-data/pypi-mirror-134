# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['glitor']

package_data = \
{'': ['*']}

install_requires = \
['docker>=5.0.3,<6.0.0',
 'fastapi-utils>=0.2.1,<0.3.0',
 'fastapi>=0.71.0,<0.72.0',
 'gunicorn>=20.1.0,<21.0.0',
 'uvicorn>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'glitor',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Md Moin Uddin',
    'author_email': 'moensam@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
