# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geobook']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'geobook',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Aliaksandr Vaskevich',
    'author_email': 'vaskevic.an@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gb-libs/geobook',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
