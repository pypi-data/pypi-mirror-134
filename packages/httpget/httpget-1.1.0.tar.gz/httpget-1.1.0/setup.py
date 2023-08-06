# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['httpget']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=4.0.1,<5.0.0', 'requests>=2.27.1,<3.0.0', 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'httpget',
    'version': '1.1.0',
    'description': 'Download files using http',
    'long_description': None,
    'author': 'Wissem Mansouri',
    'author_email': 'wissem.mansouri.ing@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
