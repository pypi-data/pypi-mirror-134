# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['begin', 'begin.cli']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['begin = begin.cli.cli:main']}

setup_kwargs = {
    'name': 'begin-cli',
    'version': '0.0.1',
    'description': 'A utility for running targets in a targets.py file',
    'long_description': '# `begin` v0.0.1',
    'author': 'Lachlan Marnham',
    'author_email': None,
    'maintainer': 'Lachlan Marnham',
    'maintainer_email': None,
    'url': 'https://github.com/LachlanMarnham/begin',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.8',
}


setup(**setup_kwargs)
