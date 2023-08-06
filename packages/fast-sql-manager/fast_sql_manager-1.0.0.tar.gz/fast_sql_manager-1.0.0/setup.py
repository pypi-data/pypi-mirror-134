# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fast_sql_manager']

package_data = \
{'': ['*']}

install_requires = \
['mysql-connector-python>=8.0.27,<9.0.0']

setup_kwargs = {
    'name': 'fast-sql-manager',
    'version': '1.0.0',
    'description': 'Um pacote simples para realizar operações no banco',
    'long_description': None,
    'author': 'OscarSilvaOfficial',
    'author_email': 'oscarkaka222@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
