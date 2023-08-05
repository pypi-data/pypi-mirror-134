# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hnget']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.6.3,<5.0.0', 'requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['hnget = hnget.application:main']}

setup_kwargs = {
    'name': 'hnget',
    'version': '0.1.1',
    'description': 'Shows and opens links on Hacker news from the terminal',
    'long_description': None,
    'author': 'Jordan Sweet',
    'author_email': 'hello@jordandsweet.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
