# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tidy_twitter']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-twitter>=3.5,<4.0',
 'pytz>=2021.3,<2022.0',
 'tqdm>=4.62.3,<5.0.0']

entry_points = \
{'console_scripts': ['tidy_twitter = tidy_twitter.cli:cli']}

setup_kwargs = {
    'name': 'tidy-twitter',
    'version': '1.1.0',
    'description': "tidy-twitter helps to clean up user's Twitter history.",
    'long_description': None,
    'author': 'Sven Varkel',
    'author_email': 'sven@wasabi.ee',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
