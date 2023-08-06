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
    'version': '0.1.6',
    'description': 'Toolkit provided by IMK at KIT',
    'long_description': '# IMK Toolkit\nCollection of methods developed by IMK\n\n## Usage\n\n```python\nimport imktk\nimport xarray as xr\n\nt = xr.tutorial.open_dataset("rasm").load().Tair\nanomaly_free_t = t.imktk.anomalies()\n```\n',
    'author': 'Uğur Çayoğlu',
    'author_email': 'Ugur.Cayoglu@kit.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/imk-toolkit/imk-toolkit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
