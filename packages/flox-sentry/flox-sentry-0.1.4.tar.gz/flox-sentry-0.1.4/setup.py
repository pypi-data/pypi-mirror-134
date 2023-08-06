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
    'version': '0.1.4',
    'description': 'Automatically create projects and teams for flox managed projects',
    'long_description': "# flox sentry integration\n\nCreate sentry project and expose DSN value for future processing during [flox](https://github.com/getflox/flox) workflow\n\n## Key features\n- create sentry project with same name as flox \n- create sentry team for each project (optional)\n- automatically create DSN for given project \n- expose DSN value as variable which can be used in project workflow or bootstrap template\n\n## Exposed variables\n\n- sentry_dsn\n\n## Installation\n\n```bash\n$ flox plugin install flox-sentry\n```\n\nor\n\n```bash\n$ pip install flox-sentry\n```\n\n## Configuration\n\n```bash\n$ flox config --plugin sentry --scope=user\n\nℹ Starting configuration of sentry for 'user' scope\n → URL to sentry [https://sentry.io/]:\n → Sentry default organization [getflox]:\n → Default team which should be used for new projects (must exists) [backend]:\nℹ 'Grant permission to teams' configuration is accepting multiple values, each in new line, enter empty value to end input, '-' to delete value\n\nNew configuration:\n\n Key                            Old value  New value\n─────────────────────────────────────────────────────\n Create a new team per project  {}         False\n Grant permission to teams      {}         -\n\nSave plugin settings? [y/N]: y\nℹ Configuration saved: /Users/user/.flox/settings.toml\n → Sentry Access Token []: -----\n\nNew configuration:\n\n Key                  Old value                                                         New value\n──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n Sentry Access Token  ------                                                            ------\n\nSave plugin settings? [y/N]: y\nℹ Updated 1 secrets\n```\n",
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
