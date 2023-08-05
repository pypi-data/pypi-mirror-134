# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esovalue']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'esovalue',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Stéphane Thibaud',
    'author_email': 'snthibaud@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
