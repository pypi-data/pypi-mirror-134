# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_remake']

package_data = \
{'': ['*'], 'nonebot_plugin_remake': ['resources/*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-remake',
    'version': '0.2.2',
    'description': '适用于 Nonebot2 的人生重开模拟器插件',
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
