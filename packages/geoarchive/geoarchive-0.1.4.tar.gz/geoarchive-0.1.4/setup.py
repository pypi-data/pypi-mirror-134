# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geoarchive']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.5,<2.0.0', 'pycountry>=22.1.10,<23.0.0', 'pyzotero>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'geoarchive',
    'version': '0.1.4',
    'description': 'Utilities for the USGS GeoArchive',
    'long_description': '# GeoArchive\n\nThe GeoArchive is a loosely coupled architecture of interoperating diverse repositories containing important geoscientific data, information, and knowledge content. Through a software layer, the GeoArchive coordinates actions across these repositories to ensure their near and long-term viability as scientific assets. This Python package is one element of the software layer.\n\n## Documentation\n\n[GitHub Pages](https://skybristol.github.io/geoarchive/)\n\n## Installing\n\n```bash\npip install geoarchive\n```',
    'author': 'Sky Bristol',
    'author_email': 'sbristol@usgs.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/skybristol/geoarchive',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
