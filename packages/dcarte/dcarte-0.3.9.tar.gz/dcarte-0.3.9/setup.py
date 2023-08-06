# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dcarte', 'dcarte.derived', 'dcarte.legacy']

package_data = \
{'': ['*'], 'dcarte': ['source_yaml/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'ipykernel>=6.6.0,<7.0.0',
 'ipython>=7.30.1,<8.0.0',
 'ipywidgets>=7.6.5,<8.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'jupyterlab>=3.2.8,<4.0.0',
 'lab>=7.0,<8.0',
 'numpy>=1.21.5,<2.0.0',
 'pandas>=1.3.5,<2.0.0',
 'pyarrow>=3.0.0,<6.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.26.0,<3.0.0',
 'scipy>=1.7.3,<2.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'widgetsnbextension>=3.5.2,<4.0.0']

setup_kwargs = {
    'name': 'dcarte',
    'version': '0.3.9',
    'description': 'DCARTE is a dataset ingestion tool from DCARTE UK-DRI CAre Research and TEchnology',
    'long_description': None,
    'author': 'eyal soreq',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
