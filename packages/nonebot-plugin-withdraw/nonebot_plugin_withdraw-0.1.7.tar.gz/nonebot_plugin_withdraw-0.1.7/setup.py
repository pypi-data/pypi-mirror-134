# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_withdraw']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-cqhttp>=2.0.0-alpha.13,<2.0.0-beta.1',
 'nonebot2>=2.0.0-alpha.13,<2.0.0-beta.1']

setup_kwargs = {
    'name': 'nonebot-plugin-withdraw',
    'version': '0.1.7',
    'description': 'A simple withdraw plugin for Nonebot2',
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
