# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytorch_common',
 'pytorch_common.callbacks',
 'pytorch_common.callbacks.output',
 'pytorch_common.callbacks.output.plot',
 'pytorch_common.kfoldcv',
 'pytorch_common.kfoldcv.strategy',
 'pytorch_common.modules',
 'pytorch_common.util']

package_data = \
{'': ['*']}

install_requires = \
['bunch>=1.0.1,<2.0.0',
 'ipython>=7.31.0,<8.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.22.0,<2.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'torch>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'pytorch-common',
    'version': '0.0.3',
    'description': 'Common torch tools and extension',
    'long_description': None,
    'author': 'adrianmarino',
    'author_email': 'adrianmarino@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
