# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wrapper_b2p',
 'wrapper_b2p.wrapper_class',
 'wrapper_b2p.wrapper_class.class_abs',
 'wrapper_b2p.wrapper_class.mixin']

package_data = \
{'': ['*']}

install_requires = \
['pytest-cov>=3.0.0,<4.0.0',
 'requests>=2.26.0,<3.0.0',
 'xmltodict>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'wrapper-b2p',
    'version': '0.1.0',
    'description': 'wrapper best2pay',
    'long_description': None,
    'author': 'Aleksey',
    'author_email': 'ataraspost@gmail.com',
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
