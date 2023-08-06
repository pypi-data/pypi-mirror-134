# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sampledblib']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.29,<2.0.0']

setup_kwargs = {
    'name': 'sampledblib',
    'version': '1.0.0',
    'description': 'Python library to interface with a sample tracking database',
    'long_description': None,
    'author': 'Maxwell Murphy',
    'author_email': 'murphy2122@berkeley.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
