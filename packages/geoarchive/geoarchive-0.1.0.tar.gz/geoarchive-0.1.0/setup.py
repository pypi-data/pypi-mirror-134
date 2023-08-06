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
    'version': '0.1.0',
    'description': 'Utilities for the USGS GeoArchive',
    'long_description': '# GeoArchive\n\nThe GeoArchive is a loosely coupled architecture for adopting various kinds of data, information, and knowledge repositories as archives of important scientific material that an institution (the USGS in this case) wants to adopt for long-term curation and management. This Python package provides utilities for operating curation and management tasks in standardized ways across different types of third party technologies. The archives of the GeoArchive construct are considered "active archives" in that they may be used in practice. \n\nEnterprise archival tasks include things like:\n\n* Registering a repository for adoption\n* Reading and checking the metadata that describe items in a repository for compliance with standards and conventions that make the materials viable for archival\n* Examining, evaluating, and reporting on the digital contents of a repository, classifying materials as to their long-term viability and recommended actions for curation\n* Pulling all or select materials from a participating repository into a long-term backup/storage solution\n* Registering links for a repository\'s items through a handle system for the purpose of creating long-lasting references\n* Creating additional linkages for the items in a repository and/or descriptive metadata to other information sources inside or outside the GeoArchive framework (e.g., between repositories known to the GeoArchive, between items in a GeoArchive repository and third party information systems)',
    'author': 'Sky Bristol',
    'author_email': 'sbristol@usgs.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
