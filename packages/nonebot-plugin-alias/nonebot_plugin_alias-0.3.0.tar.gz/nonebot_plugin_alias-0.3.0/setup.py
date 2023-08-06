# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_alias']

package_data = \
{'': ['*']}

install_requires = \
['expandvars>=0.7.0,<0.8.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-alias',
    'version': '0.3.0',
    'description': 'A simple plugin for adding aliases for Nonebot command',
    'long_description': None,
    'author': 'meetwq',
    'author_email': 'meetwq@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
