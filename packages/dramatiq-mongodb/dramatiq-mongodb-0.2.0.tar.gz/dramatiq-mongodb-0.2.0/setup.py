# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dramatiq_mongodb']

package_data = \
{'': ['*']}

install_requires = \
['dramatiq>=1.12.1,<2.0.0', 'pymongo>=4.0.1,<5.0.0']

setup_kwargs = {
    'name': 'dramatiq-mongodb',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Tory Clasen',
    'author_email': 'ToryClasen@Gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
