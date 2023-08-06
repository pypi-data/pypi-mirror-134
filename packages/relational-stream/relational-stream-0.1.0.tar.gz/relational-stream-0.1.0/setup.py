# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['relational_stream']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=6.2.5,<7.0.0']

entry_points = \
{'console_scripts': ['amt = apple_music_tools.main:app']}

setup_kwargs = {
    'name': 'relational-stream',
    'version': '0.1.0',
    'description': 'A Python library for relational stream analysis.',
    'long_description': None,
    'author': 'Stephan Lensky',
    'author_email': 'stephanl.public@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stephanlensky/python-relational-stream-analysis',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
