# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsw_nx', 'jsw_nx.base', 'jsw_nx.packages']

package_data = \
{'': ['*'], 'jsw_nx': ['classes/*']}

setup_kwargs = {
    'name': 'jsw-nx',
    'version': '1.0.4',
    'description': 'Next toolkit for python.',
    'long_description': '# jsw-nx\n> Next toolkit for python.',
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
