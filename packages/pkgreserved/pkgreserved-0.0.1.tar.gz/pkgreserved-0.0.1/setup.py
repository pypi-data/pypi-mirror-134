# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pkgreserved']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pkgreserved',
    'version': '0.0.1',
    'description': 'Description',
    'long_description': None,
    'author': 'Reserver',
    'author_email': 'reserving.package.name@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
