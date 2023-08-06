# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shakah',
 'shakah._core',
 'shakah.gears',
 'shakah.gears.structs',
 'shakah.models',
 'shakah.utils',
 'shakah.utils.decorators']

package_data = \
{'': ['*']}

install_requires = \
['cytoolz>=0.11.2,<0.12.0',
 'decorator>=5.1.1,<6.0.0',
 'devtools>=0.8.0,<0.9.0',
 'dynaconf[vault,redis]>=3.1.7,<4.0.0',
 'fastcore>=1.3.27,<2.0.0',
 'import-linter>=1.2.6,<2.0.0',
 'loguru>=0.5.3,<0.6.0',
 'psycopg2>=2.9.3,<3.0.0',
 'pydantic[dotenv,email]>=1.9.0,<2.0.0',
 'sqlmodel>=0.0.6,<0.0.7']

setup_kwargs = {
    'name': 'shakah',
    'version': '2.0.0',
    'description': '',
    'long_description': '',
    'author': 'kivo360',
    'author_email': 'kivo360@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
