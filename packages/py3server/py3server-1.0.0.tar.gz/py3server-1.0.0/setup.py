# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py3server',
 'py3server.app',
 'py3server.utils',
 'py3server.web',
 'py3server.web.controllers',
 'py3server.web.mapping',
 'py3server.web.params']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py3server',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'Florian',
    'author_email': 'dev.florianbematol@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
