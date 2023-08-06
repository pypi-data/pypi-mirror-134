# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flox_git']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.0,<4.0.0', 'flox-core>=0.2,<1.0.0']

entry_points = \
{'flox.plugin': ['git = flox_git:plugin']}

setup_kwargs = {
    'name': 'flox-git',
    'version': '0.2.0',
    'description': 'Bootstrap git repository for your project managed by flox.',
    'long_description': None,
    'author': 'Michal Przytulski',
    'author_email': 'michal@przytulski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/getflox/flox-git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
