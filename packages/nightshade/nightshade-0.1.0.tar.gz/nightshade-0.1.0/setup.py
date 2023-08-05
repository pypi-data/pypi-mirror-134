# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nightshade']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.10.0,<5.0.0',
 'click>=8.0.3,<9.0.0',
 'nltk>=3.6.5,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['nightshade = nightshade:nightshade']}

setup_kwargs = {
    'name': 'nightshade',
    'version': '0.1.0',
    'description': 'Tools for retrieving movie data from Rotten Tomatoes',
    'long_description': None,
    'author': 'Roni Choudhury',
    'author_email': 'aichoudh@gmail.com',
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
