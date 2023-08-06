# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ngsildclient',
 'ngsildclient.api',
 'ngsildclient.model',
 'ngsildclient.model.helper',
 'ngsildclient.playground',
 'ngsildclient.utils']

package_data = \
{'': ['*']}

install_requires = \
['geojson>=2.5.0,<3.0.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'ngsildclient',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'fbattello',
    'author_email': 'fabien.battello@orange.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
