# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wildcard_matcher']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'wildcard-matcher',
    'version': '0.0.1',
    'description': 'A simple wildcard string matcher',
    'long_description': None,
    'author': 'James Hodgkinson',
    'author_email': 'james@terminaloutcomes.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
