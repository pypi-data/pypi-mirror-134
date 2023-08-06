# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wildcard_matcher']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'wildcard-matcher',
    'version': '0.0.2',
    'description': 'A simple wildcard string matcher',
    'long_description': '# wildcard_matcher\n\nA simple wildcard string matcher widget for python 3.x.\n\n# Installation\n\n```shell\npython -m pip install wildcard_matcher\n```\n\n# Usage\n\n```\n>>> import wildcard_matcher\n>>> wildcard_matcher.match("hello world", "hello*")\nTrue\n>>> wildcard_matcher.match("hello world", "he*lo*world")\nTrue\n>>> wildcard_matcher.match("hello world", "he*lo*rld")\nTrue\n```\n\n# Contributing\n\nPlease feel free to [log an issue](issues/new) with examples of what you tried and didn\'t work. PRs are most welcome.\n\n',
    'author': 'James Hodgkinson',
    'author_email': 'james@terminaloutcomes.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yaleman/wildcard_matcher',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
