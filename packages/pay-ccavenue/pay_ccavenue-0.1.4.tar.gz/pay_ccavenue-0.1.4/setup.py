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
    'version': '0.1.4',
    'description': 'A simple library to setup payment integration with CCAvenue',
    'long_description': "# pay_ccavenue\n\nA simple package to integrate CCAvenue. It can be used for both `iframe` and `seemless` methods.\n\n## How to install\n\n```bash\npip install pay_ccavenue\n```\n\n## Import\n\n```python\nfrom pay_ccavenue import CCAvenue\n```\n\n## Initialize the Package\n\nWe can either setup via the environment or by passing the credentials directly to the plugin.\n\n### Via the environment variables\n\nSet the credentials in the environment variables\n\n- Set `CCAVENUE_WORKING_KEY` for the `WORKING_KEY`\n- Set `CCAVENUE_ACCESS_CODE` for the `ACCESS_CODE`\n- Set `CCAVENUE_MERCHANT_CODE` for the `MERCHANT_CODE`\n\nAnd then instantiate the `CCAvenue` object as shown below\n\n```python\nccavenue = CCAvenue()\n```\n\n### Pasing the credentials directly\n\n```python\nccavenue = CCAvenue(WORKING_KEY, ACCESS_CODE, MERCHANT_CODE)\n```\n\n## To encrypt the data\n\n`form_data` is the post request body which is a dictionary of the related data for the payment. You don't need to pass the Merchant ID though. Since we have already intiated the package with the correct `MERCHANT_CODE`. `encrypt()` method return the encrypted string that can be ussed directly in the Iframe rendering.\n\n```python\nencrypt_data = ccavenue.encrypt(form_data)\n```\n\nPass the `encrypt_data` from the above to the view to render the IFrame.\n\n## Decrypt the data received from the CCAvenue\n\n`form_data` is the post request body which is a dictionary of the related data received from the CCAvenue. The `decrypt()` method returns the dictionary of the data received from the CCAvenue.\n\n```python\ndecrypted_data = ccavenue.decrypt(form_data)\n```\n\n# Limitations\n\n1. I have not added any tests as of now in the package, but I have tested this out for my project after debugging their given examples and Stackoverflow to simplify it.\n2. More detailed documentation.\n",
    'author': 'Kuldeep Pisda',
    'author_email': 'pisdak79@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kdpisda/python-pay-ccavenue',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
