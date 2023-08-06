# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imgdir']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['imgdir = imgdir.console:run']}

setup_kwargs = {
    'name': 'imgdir',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'zenwalk',
    'author_email': 'zenwalk@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
