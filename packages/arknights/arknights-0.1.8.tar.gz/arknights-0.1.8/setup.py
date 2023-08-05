# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arknights']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.21.3,<0.22.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'arknights',
    'version': '0.1.8',
    'description': 'arknights CN request functions',
    'long_description': None,
    'author': 'djkcyl',
    'author_email': 'cyl@cyllive.cn',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/djkcyl/py_arknights',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
