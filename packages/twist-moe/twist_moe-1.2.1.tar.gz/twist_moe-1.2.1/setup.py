# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twist_moe']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome', 'requests']

extras_require = \
{':sys_platform == "win32"': ['windows-curses']}

entry_points = \
{'console_scripts': ['twist = twist_moe.tui:main']}

setup_kwargs = {
    'name': 'twist-moe',
    'version': '1.2.1',
    'description': 'twist.moe client',
    'long_description': None,
    'author': 'witherornot',
    'author_email': 'damemem@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
