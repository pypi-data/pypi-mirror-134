# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flox_sentry']

package_data = \
{'': ['*']}

install_requires = \
['flox-core>=0.2,<1.0.0',
 'python-slugify>=4.0,<5.0',
 'requests-toolbelt>=0.9,<0.10']

entry_points = \
{'flox.plugin': ['sentry = flox_sentry:plugin']}

setup_kwargs = {
    'name': 'flox-sentry',
    'version': '0.1.3',
    'description': 'Automatically create projects and teams for flox managed projects',
    'long_description': None,
    'author': 'Michal Przytulski',
    'author_email': 'michal@przytulski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/getflox/flox-sentry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
