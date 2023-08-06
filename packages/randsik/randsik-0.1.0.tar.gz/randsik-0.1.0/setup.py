# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['randsik', 'randsik.song_builder']

package_data = \
{'': ['*'],
 'randsik': ['midi/drums/blues/*', 'midi/drums/funk/*', 'midi/drums/rock/*']}

install_requires = \
['mido>=1.2.10,<2.0.0']

setup_kwargs = {
    'name': 'randsik',
    'version': '0.1.0',
    'description': 'library for generating random music in Python',
    'long_description': None,
    'author': 'Travis Hathaway',
    'author_email': 'travis.j.hathaway@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
