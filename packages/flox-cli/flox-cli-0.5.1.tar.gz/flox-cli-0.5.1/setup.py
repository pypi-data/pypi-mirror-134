# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flox',
 'flox.config',
 'flox.info',
 'flox.plugins',
 'flox.profile',
 'flox.project',
 'flox.utils']

package_data = \
{'': ['*']}

install_requires = \
['anyconfig>=0.10,<0.11',
 'click-plugins>=1.1.1,<2.0.0',
 'click-shell>=2.0,<3.0',
 'click>=7.1,<8.0',
 'colorama>=0.4,<0.5',
 'deepmerge>=1.0,<2.0',
 'dictdiffer>=0.9,<0.10',
 'flox-core>=0.2,<1.0.0',
 'humanfriendly>=10.0,<11.0',
 'keyring>=21,<22',
 'plumbum>=1.6,<2.0',
 'pygments>=2.5,<3.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.23.0,<3.0.0',
 'schema>=0.7,<0.8',
 'slugify>=0.0.1,<0.0.2',
 'terminaltables>=3.1.0,<4.0.0']

extras_require = \
{'bootstrap': ['flox-bootstrap>=0.1,<1.0.0'],
 'git': ['flox-git>=0.1,<1.0.0'],
 'github': ['flox-github>=0.1,<1.0.0'],
 'sentry': ['flox-sentry>=0.1,<1.0.0']}

entry_points = \
{'console_scripts': ['flox = flox.cli:cli'],
 'flox.plugin': ['global = flox:plugin']}

setup_kwargs = {
    'name': 'flox-cli',
    'version': '0.5.1',
    'description': 'Highly opinionated workflow and orchestration toolkit for modern microservice development',
    'long_description': None,
    'author': 'Michal Przytulski',
    'author_email': 'michal@przytulski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/getflox/flox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
