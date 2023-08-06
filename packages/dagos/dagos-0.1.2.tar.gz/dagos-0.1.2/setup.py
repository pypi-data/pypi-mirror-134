# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagos',
 'dagos.commands',
 'dagos.commands.manage',
 'dagos.commands.manage.components',
 'dagos.commands.manage.components.git',
 'dagos.commands.wsl',
 'dagos.utils']

package_data = \
{'': ['*']}

install_requires = \
['click-option-group>=0.5.3,<0.6.0',
 'click>=8.0.3,<9.0.0',
 'rich>=11.0.0,<12.0.0']

setup_kwargs = {
    'name': 'dagos',
    'version': '0.1.2',
    'description': 'A CLI for managing software environments.',
    'long_description': None,
    'author': 'Lucas Resch',
    'author_email': 'lucas.resch@gmx.de',
    'maintainer': 'Lucas Resch',
    'maintainer_email': 'lucas.resch@gmx.de',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
