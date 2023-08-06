# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['potreepublisher']

package_data = \
{'': ['*'], 'potreepublisher': ['viewer_templates/*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['PotreePublisher = potreepublisher.main:app']}

setup_kwargs = {
    'name': 'potreepublisher',
    'version': '0.1.0',
    'description': 'Small CLI to quickly publish a single LAS file or a whole folder to a Potree server.',
    'long_description': '# PotreePublisher\nSmall CLI to quickly publish a single LAS file or a whole folder to a Potree server.\n```\nUsage: PotreePublisher [OPTIONS] INPUT_PATH\n\nArguments:\n  INPUT_PATH  Path to the point cloud or a folder of point clouds to process.\n              Any type supported by PotreeConverter is possible.  [required]\n\nOptions:\n  --potree-server-root TEXT  Root path of the potree server.  [default:\n                             /var/www/potree]\n  --point-cloud-folder TEXT  Folder where the point cloud will be stored after\n                             conversion to Potree Format.  [default:\n                             pointclouds]\n  --viewer-folder TEXT       Folder where the viewer html page will be stored.\n                             [default: results]\n  --help                     Show this message and exit.\n```\n## Installation\nInstallation instructions coming soon!\n\n',
    'author': 'Elie-Alban LESCOUT',
    'author_email': 'elie-alban.lescout@ensg.eu',
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
