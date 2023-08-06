# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_shindan']

package_data = \
{'': ['*'], 'nonebot_plugin_shindan': ['templates/*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'httpx>=0.19.0',
 'lxml>=4.6.5,<5.0.0',
 'nonebot-adapter-cqhttp>=2.0.0-alpha.15,<2.0.0-beta.1',
 'nonebot-plugin-htmlrender>=0.0.1',
 'nonebot2>=2.0.0-alpha.15,<2.0.0-beta.1',
 'playwright>=1.9.2,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-shindan',
    'version': '0.1.9',
    'description': 'Nonebot2 plugin for using ShindanMaker',
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
