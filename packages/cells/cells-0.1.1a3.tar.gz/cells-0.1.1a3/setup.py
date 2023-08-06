# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cells', 'cells.databases']

package_data = \
{'': ['*']}

install_requires = \
['pytest-cov>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'cells',
    'version': '0.1.1a3',
    'description': '',
    'long_description': None,
    'author': 'Darren Burns',
    'author_email': 'darren@textualize.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
