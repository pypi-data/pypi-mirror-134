# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['f8c']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'flake8-codes>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['f8c = f8c.cli:cli']}

setup_kwargs = {
    'name': 'f8c',
    'version': '0.1.2',
    'description': 'cli wrapper around flake8_codes',
    'long_description': "f8c\n======================\n\nProvides a conventional cli entrypoint as a thin wrapper around\n`flake8_codes <https://github.com/orsinium-labs/flake8-codes/tree/master/flake8_codes>`_ so that\nI can install it with `pipx <https://pypa.github.io/pipx/>`_. That's it.\n\nIf you work in projects that use any flake8 plugins that provide new error\ncodes, you will need to install f8c in the local venv to introspect them.\n\nActually, you should probably just use flake8_codes as indicated in its README\nand not use f8c at all.\n\nInstallation\n------------\n\n.. code-block :: console\n\n    pip3 install f8c\n\nUsage\n-----\n\n.. code-block :: console\n\n    $ f8c w6\n    pycodestyle          | W601     | .has_key() is deprecated, use 'in'\n    pycodestyle          | W602     | deprecated form of raising exception\n    pycodestyle          | W603     | '<>' is deprecated, use '!='\n    pycodestyle          | W604     | backticks are deprecated, use 'repr()'\n    pycodestyle          | W605     | invalid escape sequence '\\%s'\n    pycodestyle          | W606     | 'async' and 'await' are reserved keywords starting with Python 3.7\n",
    'author': 'Ryan Delaney',
    'author_email': 'ryan.patrick.delaney@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/f8c',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
