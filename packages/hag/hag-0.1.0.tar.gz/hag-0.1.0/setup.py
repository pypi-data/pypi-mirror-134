# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hag', 'hag.displays', 'hag.extractors', 'hag.extractors.sources']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['hag = hag.__main__:main']}

setup_kwargs = {
    'name': 'hag',
    'version': '0.1.0',
    'description': 'A hotkey aggregator. All your hotkeys in one place.',
    'long_description': None,
    'author': 'Loic Coyle',
    'author_email': 'loic.coyle@hotmail.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
