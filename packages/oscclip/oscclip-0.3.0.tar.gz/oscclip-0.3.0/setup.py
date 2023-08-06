# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oscclip']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['osc-copy = oscclip:osc_copy',
                     'osc-paste = oscclip:osc_paste']}

setup_kwargs = {
    'name': 'oscclip',
    'version': '0.3.0',
    'description': 'Utilities to access the clipboard via OSC52',
    'long_description': None,
    'author': 'Stefan Tatschner',
    'author_email': 'stefan@rumpelsepp.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
