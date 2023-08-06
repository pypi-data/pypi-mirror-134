# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schemasheets', 'schemasheets.conf', 'schemasheets.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'bioregistry>=0.4.30,<0.5.0',
 'linkml>=1.1.15,<2.0.0',
 'ontodev-cogs>=0.3.3,<0.4.0']

entry_points = \
{'console_scripts': ['sheets2linkml = fairstructure.schemamaker:convert',
                     'sheets2project = '
                     'fairstructure.sheets_to_project:multigen']}

setup_kwargs = {
    'name': 'schemasheets',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'cmungall',
    'author_email': 'cjm@berkeleybop.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
