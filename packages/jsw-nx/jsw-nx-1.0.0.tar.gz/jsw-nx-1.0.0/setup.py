# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsw_nx', 'jsw_nx.base']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jsw-nx',
    'version': '1.0.0',
    'description': 'Next toolkit for python.',
    'long_description': None,
    'author': 'feizheng',
    'author_email': '1290657123@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
