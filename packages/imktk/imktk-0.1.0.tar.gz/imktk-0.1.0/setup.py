# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imktk', 'imktk.dataarray_methods']

package_data = \
{'': ['*'], 'imktk': ['dataset_methods/*']}

install_requires = \
['netCDF4>=1.5.8,<2.0.0', 'xarray>=0.20.1,<0.21.0']

entry_points = \
{'console_scripts': ['imktk = imktk:main']}

setup_kwargs = {
    'name': 'imktk',
    'version': '0.1.0',
    'description': 'Toolkit provided by IMK at KIT',
    'long_description': None,
    'author': 'Uğur Çayoğlu',
    'author_email': 'cayoglu@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
