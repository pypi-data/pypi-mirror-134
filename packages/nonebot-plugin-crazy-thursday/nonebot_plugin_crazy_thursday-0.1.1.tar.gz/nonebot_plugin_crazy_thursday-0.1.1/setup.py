# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_crazy_thursday']

package_data = \
{'': ['*'], 'nonebot_plugin_crazy_thursday': ['resource/*']}

setup_kwargs = {
    'name': 'nonebot-plugin-crazy-thursday',
    'version': '0.1.1',
    'description': 'Send crazy thursday articles of KFC randomly!',
    'long_description': None,
    'author': 'KafCoppelia',
    'author_email': 'k740677208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.3',
}


setup(**setup_kwargs)
