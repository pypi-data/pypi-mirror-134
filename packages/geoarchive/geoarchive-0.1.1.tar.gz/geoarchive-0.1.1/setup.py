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
    'version': '0.1.1',
    'description': 'Utilities for the USGS GeoArchive',
    'long_description': '# GeoArchive\n\nThe GeoArchive is a loosely coupled architecture for adopting various kinds of data, information, and knowledge repositories as archives of important scientific material that an institution (the USGS in this case) wants to adopt for long-term curation and management. The archives of the GeoArchive construct are considered "active archives" in that they may be used in practice. This Python package provides utilities for operating curation and management tasks in standardized ways across different types of third party technologies. \n\nEnterprise archival tasks include things like:\n\n* Registering a repository for adoption\n* Reading and checking the metadata that describe items in a repository for compliance with standards and conventions that make the materials viable for archival\n* Examining, evaluating, and reporting on the digital contents of a repository, classifying materials as to their long-term viability and recommended actions for curation\n* Pulling all or select materials from a participating repository into a long-term backup/storage solution\n* Registering links for a repository\'s items through a handle system for the purpose of creating long-lasting references\n* Creating additional linkages for the items in a repository and/or descriptive metadata to other information sources inside or outside the GeoArchive framework (e.g., between repositories known to the GeoArchive, between items in a GeoArchive repository and third party information systems)\n\nNote: This is a work in progress project that has certain aspects which are highly tuned specifically to the USGS and what we are doing with this concept. We will be working to generalize functionality over time such that it may prove useful to others as well.\n\n## Installing\n\n```\npip install geoarchive\n```\n\n## Modules\n\nWe are designing the package to contain individual modules for interacting with different types of third party repository systems that serve as sources for GeoArchive collections. Each module has its own specific requirements and dependencies for what it needs to do to make its specific connections. All modules will likely require some type of specific connection information.\n\n### Zotero\n\nOur initial use case is for using a Zotero group library as a repository of document-type materials. This module leverages the pyzotero package to create an instance of an API connection to a specified Group Library in Zotero and a set of functions for working with that connection in a variety of ways. It requires a library_id and an api_key, which can be supplied through environment variables or through passed variables in instantiating the connection. Certain functionality also requires the specification of a inventory_item, which is the identifier for a specific item stored in the library that contains a cache of metadata.\n\n',
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
