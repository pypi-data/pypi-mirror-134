# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pay_ccavenue']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome==3.12.0']

setup_kwargs = {
    'name': 'pay-ccavenue',
    'version': '0.1.2',
    'description': 'A simple library to setup payment integration with CCAvenue',
    'long_description': None,
    'author': 'Kuldeep Pisda',
    'author_email': '22424149+kdpisda@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
