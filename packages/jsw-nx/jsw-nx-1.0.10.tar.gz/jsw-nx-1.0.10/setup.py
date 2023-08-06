# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsw_nx', 'jsw_nx.base', 'jsw_nx.packages', 'jsw_nx.rubify']

package_data = \
{'': ['*'], 'jsw_nx': ['classes/*']}

setup_kwargs = {
    'name': 'jsw-nx',
    'version': '1.0.10',
    'description': 'Next toolkit for python.',
    'long_description': '# jsw-nx\n> Next toolkit for python.\n\n## installation\n```shell\npip install jsw-nx\n```\n\n## usage\n```python\nimport jsw_nx as nx\n\n## common methods\nnx.includes([1,2,3], 2) # => True\nnx.includes([1,2,3], 5) # => False\n```\n\n## next core methods\n- base/filter\n- base/find\n- base/find_index\n- base/foreach\n- base/forin\n- base/get\n- base/includes\n- base/indexof\n- base/map\n- base/reduce\n- base/set\n\n## ruby style\n- rubify/to_f\n- rubify/to_i\n- rubify/to_n\n- rubify/to_s\n\n## next packages\n- days',
    'author': 'feizheng',
    'author_email': '1290657123@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://js.work',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
