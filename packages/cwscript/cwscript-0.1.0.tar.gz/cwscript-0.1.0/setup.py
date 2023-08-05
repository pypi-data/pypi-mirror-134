# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cwsc',
 'cwscript',
 'cwscript.lang',
 'cwscript.lang.grammar',
 'cwscript.util',
 'cwsls']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'Pygments>=2.11.2,<3.0.0',
 'antlr4-python3-runtime>=4.9.3,<5.0.0',
 'click>=8.0.3,<9.0.0',
 'prompt-toolkit>=3.0.24,<4.0.0',
 'pygls>=0.11.3,<0.12.0',
 'python-fire>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['cws-highlight = cwscript.highlight:main',
                     'cwsc = cwsc:main',
                     'cwsls = cwsls:start_server']}

setup_kwargs = {
    'name': 'cwscript',
    'version': '0.1.0',
    'description': 'CWScript compiler and standard tooling.',
    'long_description': None,
    'author': 'William Chen',
    'author_email': 'william@terran.one',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
