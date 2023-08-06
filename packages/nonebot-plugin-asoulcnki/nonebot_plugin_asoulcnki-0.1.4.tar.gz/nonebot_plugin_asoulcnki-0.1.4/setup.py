# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_asoulcnki']

package_data = \
{'': ['*'], 'nonebot_plugin_asoulcnki': ['templates/*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'httpx>=0.19.0',
 'nonebot-adapter-cqhttp>=2.0.0-alpha.15,<2.0.0-beta.1',
 'nonebot-plugin-htmlrender>=0.0.1',
 'nonebot2>=2.0.0-alpha.15,<2.0.0-beta.1']

setup_kwargs = {
    'name': 'nonebot-plugin-asoulcnki',
    'version': '0.1.4',
    'description': 'ASoulCnki plugin for Nonebot2',
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
