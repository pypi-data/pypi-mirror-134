# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlcraft']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mlcraft',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Praveen Kulkarni',
    'author_email': 'praveenneuron@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
