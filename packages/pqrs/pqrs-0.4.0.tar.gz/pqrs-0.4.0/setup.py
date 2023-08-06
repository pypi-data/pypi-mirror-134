# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pqrs']

package_data = \
{'': ['*']}

install_requires = \
['ansible-runner>=1.4.7,<2.0.0',
 'ansible>=3.2.0,<4.0.0',
 'datafiles>=0.15,<0.16',
 'plumbum>=1.7.0,<2.0.0',
 'pq-npyscreen>=4.9.1,<5.0.0',
 'semantic-version>=2.8.5,<3.0.0',
 'temppathlib>=1.1.0,<2.0.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['pqrs = pqrs.cli:run']}

setup_kwargs = {
    'name': 'pqrs',
    'version': '0.4.0',
    'description': 'CLI tool to manage Linux workstations.',
    'long_description': None,
    'author': 'ProteinQure team',
    'author_email': 'team@proteinqure.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
