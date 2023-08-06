# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['terraform_install']

package_data = \
{'': ['*']}

install_requires = \
['terraform_version']

setup_kwargs = {
    'name': 'terraform-install',
    'version': '0.1.1',
    'description': 'Installs Terraform to virtualenv bin',
    'long_description': None,
    'author': 'Josh Wycuff',
    'author_email': 'Joshua.Wycuff@turner.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
