# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graph']

package_data = \
{'': ['*']}

install_requires = \
['retworkx>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'graph-wrapper',
    'version': '1.0.0',
    'description': 'Wrapped of popular network libraries with type annotations',
    'long_description': None,
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/binh-vu/graph',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
