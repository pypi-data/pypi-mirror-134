# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poglossary']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'polib>=1.1.1,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'tabulate[widechars]>=0.8.9,<0.9.0',
 'typer[all]>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'poglossary',
    'version': '0.1.0',
    'description': 'A CLI tool that scans through .po files and searches for mistranslated terms based on user-defined glossary mapping',
    'long_description': None,
    'author': 'Matt.Wang',
    'author_email': 'mattwang44@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
