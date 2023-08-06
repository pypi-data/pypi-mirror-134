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

entry_points = \
{'console_scripts': ['poglossary = poglossary.poglossary:app']}

setup_kwargs = {
    'name': 'poglossary',
    'version': '0.1.2',
    'description': 'A CLI tool that scans through .po files and searches for mistranslated terms based on user-defined glossary mapping',
    'long_description': '# poglossary\n\nA CLI tool that scans through translation project (`.po` files) searching for mistranslated terms based on the user-defined glossary mapping.\n\nThis project is special tailored for [Python Documentation Translation Project (zh_TW)](https://github.com/python/python-docs-zh-tw) but can be applied for all translation projects that use Portable Object files (`.po`).\n\n## Usage\n\n```yml\n# Sample config file (.yml)\nglossary:\n  exception: 例外\n  function: 函式\n  instance: 實例\n  type: # can be a list of possible translated terms\n    - 型別\n    - 種類\n```\n\n```sh\n> python poglossary --help\n\n# Usage: python -m poglossary [OPTIONS] [PATH] [CONFIG_FILE]\n\n#   poglossary: check translated content in .po files based on given translation\n#   mapping\n\n# Arguments:\n#   [PATH]         the path of the directory storing .po files  [default: .]\n#   [CONFIG_FILE]  input mapping file  [default: ./poglossary.yml]\n\n# Options:\n#   --excludes PATH       the directories that need to be omitted\n#   --install-completion  Install completion for the current shell.\n#   --show-completion     Show completion for the current shell, to copy it or\n#                         customize the installation.\n#   --help                Show this message and exit.\n```\n\n```shell\npoetry run python3 poglossary <source_path> <config_file>\n```\n\n## Sample Output\n\n![image](https://user-images.githubusercontent.com/24987826/149136080-357c673d-41d9-4835-8ed5-f6ef37cf625d.png)\n\n## Todo\n\n- [ ] Functionality\n  - [ ] More handy parameters/options\n- [ ] CI/CD\n  - [ ] Unit tests\n  - [ ] Static checks (mypy, isort, etc)\n  - [ ] Upload to PyPI\n- [ ] Config files\n  - [ ] Handle missing fields.\n  - [ ] Commands for creating a basic config file.\n',
    'author': 'Matt.Wang',
    'author_email': 'mattwang44@gmail.com',
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
