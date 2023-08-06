# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flox_github']

package_data = \
{'': ['*']}

install_requires = \
['flox-core>=0.2,<1.0.0', 'gitpython>=3.1.0,<4.0.0', 'pygithub>=1.46,<2.0']

entry_points = \
{'flox.plugin': ['github = flox_github:plugin']}

setup_kwargs = {
    'name': 'flox-github',
    'version': '0.2.0',
    'description': 'Create and enforce standard rules on GitHub repositories managed by flox.',
    'long_description': None,
    'author': 'Michal Przytulski',
    'author_email': 'michal@przytulski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/getflox/flox-github',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
