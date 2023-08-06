# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wordle_api']

package_data = \
{'': ['*']}

install_requires = \
['english-words>=1.0.4,<2.0.0',
 'fastapi-camelcase>=1.0.5,<2.0.0',
 'fastapi>=0.71.0,<0.72.0',
 'numpy>=1.22.0,<2.0.0',
 'uvicorn>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'wordle-api',
    'version': '1.1.0',
    'description': '',
    'long_description': None,
    'author': None,
    'author_email': None,
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
