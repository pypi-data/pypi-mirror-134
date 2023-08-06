# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_timestamps']

package_data = \
{'': ['*'], 'pytest_timestamps': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}

install_requires = \
['pytest>=5.2']

entry_points = \
{'pytest11': ['timestamps = pytest_timestamps.plugin']}

setup_kwargs = {
    'name': 'pytest-timestamps',
    'version': '0.1.3',
    'description': 'A simple plugin to view timestamps for each test',
    'long_description': None,
    'author': 'TJ',
    'author_email': 'tbruno25@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
