# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_caiyunai']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.19.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot-plugin-htmlrender>=0.0.1',
 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-caiyunai',
    'version': '0.2.0',
    'description': '适用于 Nonebot2 的彩云小梦AI续写插件',
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
