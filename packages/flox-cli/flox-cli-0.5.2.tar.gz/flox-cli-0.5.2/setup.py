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
    'version': '0.5.2',
    'description': 'Highly opinionated workflow and orchestration toolkit for modern microservice development',
    'long_description': '# flox\n\nFlox is an opinionated orchestration and automation tool for microservice development using modern stack.\n\n> Flox is under active development by amazing developers working at @epsyhealth where we\'re on a mission to give the world a better way to live with epilepsy.\n> If you would like to join us to work on even more exciting projects, visit our website: https://www.epsyhealth.com/careers\n\n\nWith flox we aim to automate the boring parts of project creation letting you focus on your business logic.\n\nFlox has a modular architecture, allowing you to extend its functionality with plugins.\n\nFlox can:\n\n- Create git repository (with [flox-git](https://github.com/getflox/flox-git))\n- Create and configure GitHub repositories (with [flox-github](https://github.com/getflox/flox-github))\n- Create sentry project and integrate it with your project (with [flox-sentry](https://github.com/getflox/flox-sentry))\n- Bootstrap your project using your own templates (with [flox-bootstrap](https://github.com/getflox/flox-git))\n\nSoon to see:\n\n- AWS integration\n- Terraform support\n- Serverless support\n\n## Key features\n\n- Multi level configuration support (define system, user and project level configuration)\n- Support for secrets with native system keyring support \n- Plugin architecture with build-in plugin manager\n- Workflow support (automatically create branches, PR and more...)\n- Support for multiple profiles (prod, dev... name it)\n- Interactive configuration management based on the plugin requirements \n- Work in command line mode or in interactive shell\n\n## Configuration\n\nFlox supports hierarchical configuration with merging and overwriting support on each level, with possibility with \ncustom configuration per profile. \n\nCurrent configuration load order:\n* /etc/flox/settings.toml\n* /etc/flox/settings.{profile}.toml\n* ~/.flox/settings.toml\n* ~/.flox/settings.{profile}.toml\n* {project_root}/.flox/settings.toml\n* {project_root}/.flox/settings.{profile}.toml\n\nGlobal configuration of the flox system itself is defined under `global` section , while each plugin\nhas it\'s own dedicated section.  \n\nAdditionally flox supports interactive environment configuration with `flox configure` command.\nConfiguration command uses plugin autodiscvery, to list all available options run `flox configure --help`.\n\n\n## Installation \n\n```bash\n$ pip install flox-cli\n```\n\noptionally you can specify extra features to be installed at the same time:\n\n```bash\n$ pip install flox-cli[git,github,bootstrap,sentry]\n```\n\n```bash\n$ flox --help\nUsage: flox [OPTIONS] COMMAND [ARGS]...\n\n  Consistent project management and automation with flox\n\nOptions:\n  -v      Verbose mode - show debug info\n  --help  Show this message and exit.\n\nCommands:\n  config   Run configuration wizard for flox.\n  plugin   Manage plugins\n  project  Initialise new project with flox\n```\n\n### Plugin management\n\nList all installed plugins\n\n```bash\n$ flox plugin \n\n name       description                                                                                url                                     version\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n global     Highly opinionated workflow and orchestration toolkit for modern microservice development  https://github.com/getflox/flox         0.5.0\n git        Bootstrap git repository for your project managed by flox.                                 https://github.com/getflox/flox-git     0.2.0\n github     Create and enforce standard rules on GitHub repositories managed by flox.                  https://github.com/getflox/flox-github  0.1.2\n bootstrap                                                                                             None                                    0.1.2\n sentry     Automatically create projects and teams for flox managed projects                          https://github.com/getflox/flox-sentry  0.1.2\n```\n\nSearch and install flox plugin\n\n```bash\nflox plugin search aws\nflox plugin install flox-aws\n```\n\n### Project creation\n\nWith flox you can quickly create a new project to work on - please remember that flox relays on the plugins, so \nyou must first install and configure plugins to see the real power of flox.\n\nExample below was executed with git, github, bootstrap and sentry plugins installed. \n\n```bash\n$ flox project --templates python --templates serverless-python                                                                                                                                                                                                                                                    11:53:39\nEnter project name: Flox Project\nEnter project description: Sample project created with flox\n✔ [github]  Created GitHub repository \'https://github.com/getflox/flox-project\'\n✔ [git]  Initialised git repository\n✔ [git]  Added new remote origin with github.com/getflox/flox-project.git\n✔ [git]  Created new master branch\n✔ [git]  Switched to master branch\n✔ [sentry]  Project "flox-project" created\nBootstraps project with given templates:  46%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▌                                                                                                                                                          | 6/13\n → Python Version [3.8.12]:\n → Enable xray support [Y/n]:\nℹ [bootstrap]  Bootstrapping project using template: python\nℹ [bootstrap]  Bootstrapping project using template: serverless-python\n✔ [github]  Vulnerability alerts: On\n✔ [github]  Automated security fixes enabled\n✔ [github]  Branch protection rules set for "master" branch.\n✔ [git]  Created default .gitignore: flox-project/.flox/.gitignore\n✔ [git]  Added flox meta files to git repository\n✔ [git]  Added flox bootstrapped files to git repository\nℹ [git]  Skipping branch master as branch already exists\n✔ [git]  Pushed to remote origin\n✔ [git]  Created branch develop\n✔ [sentry]  Assigned  teams to flox-project project\n✔ [git]  Pushed to remote origin\nPush changes to remote: 100%|\n\n$ ls -la ./flox-project\ndrwxr-xr-x   4 me  staff  128 Jan 13 11:54 .flox\ndrwxr-xr-x  13 me  staff  416 Jan 13 11:54 .git\n-rw-r--r--   1 me  staff    6 Jan 13 11:54 .python-version\n-rw-r--r--   1 me  staff   14 Jan 13 11:54 README.md\ndrwxr-xr-x   3 me  staff   96 Jan 13 11:54 flox__project\n-rw-r--r--   1 me  staff  424 Jan 13 11:54 package.json\n-rw-r--r--   1 me  staff  454 Jan 13 11:54 pyproject.toml\n-rw-r--r--   1 me  staff  510 Jan 13 11:54 serverless.yml.py\n```\n',
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
