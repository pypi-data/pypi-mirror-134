# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['ice', 'ice.api', 'ice.core', 'ice.llutil', 'ice.llutil.multiprocessing']

package_data = \
{'': ['*']}

install_requires = \
['multiprocess>=0.70.12,<0.71.0',
 'pycuda>=2021.1,<2022.0',
 'torch',
 'torchvision>=0.11.2,<0.12.0']

setup_kwargs = {
    'name': 'ice-learn',
    'version': '0.0.4',
    'description': 'A high-level Deep Learning framework that extends PyTorch and PyCUDA.',
    'long_description': None,
    'author': 'Yuyao Huang',
    'author_email': 'yycv.simon@protonmail.com',
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
