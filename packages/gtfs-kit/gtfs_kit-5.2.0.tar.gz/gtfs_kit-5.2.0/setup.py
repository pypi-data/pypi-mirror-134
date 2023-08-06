# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gtfs_kit']

package_data = \
{'': ['*']}

install_requires = \
['folium<1',
 'geopandas<1',
 'json2html<2',
 'pandas<2',
 'pycountry<20',
 'requests<3',
 'rtree<1',
 'shapely<2',
 'utm<1']

setup_kwargs = {
    'name': 'gtfs-kit',
    'version': '5.2.0',
    'description': 'A Python 3.7+ library for analyzing GTFS feeds.',
    'long_description': "GTFS Kit\n********\n.. image:: https://travis-ci.com/mrcagney/gtfs_kit.svg?branch=master\n    :target: https://travis-ci.come/mrcagney/gtfs_kit\n\nGTFS Kit is a Python 3.7+ kit for analyzing `General Transit Feed Specification (GTFS) <https://en.wikipedia.org/wiki/GTFS>`_ data in memory without a database.\nIt uses Pandas and Shapely to do the heavy lifting.\n\nThis project supersedes `GTFSTK <https://github.com/mrcagney/gtfstk>`_.\n\n\nInstallation\n=============\n``pip install gtfs_kit``.\n\n\nExamples\n========\nExamples are in the Jupyter notebook ``notebooks/examples.ipynb``.\n\n\nAuthors\n=========\n- Alex Raichev, 2019-09\n\n\nDocumentation\n=============\nOn Github Pages `here <https://mrcagney.github.io/gtfs_kit_docs>`_.\n\n\nNotes\n=====\n- Development status is Alpha\n- This project uses semantic versioning\n- Thanks to `MRCagney <http://www.mrcagney.com/>`_ for donating to this project\n- Constructive feedback and code contributions welcome. Please issue pull requests into the ``develop`` branch and include tests.\n- GTFS time is measured relative noon minus 12 hours, which can mess things up when crossing into daylight savings time. I don't think this issue causes any bugs in GTFS Kit, but you and i have been warned. Thanks to derhuerst for bringing this to my attention in `closed Issue 8 <https://github.com/mrcagney/gtfs_kit/issues/8#issue-1063633457>`_.\n",
    'author': 'Alex Raichev',
    'author_email': 'araichev@mrcagney.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mrcagney/gtfs_kit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
