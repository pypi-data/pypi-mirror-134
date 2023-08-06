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
    'version': '0.2.1',
    'description': 'Create and enforce standard rules on GitHub repositories managed by flox.',
    'long_description': '# GitHub integration for flox\n\n[flox](https://github.com/getflox/flox) automation for GitHub repository managmenet\n\n## Exposed variables\n\n- github_clone_url - http checkout URL \n- github_url - public URL of the repository \n- github_ssh_url - checkout URL used for git+ssh protocol\n- github_repository - repository object as fetched from GitHub API \n- `github_empty` -  True/False flag\n- `git_repository` - authenticated URL which can be used for all write operations\n\n## Installation \n\n```bash\n$ flox plugin install flox-github\n```\n\nor \n\n```bash\n$ pip install flox-github\n```\n\n\n## Configuration \n\n```bash\n$ flox config --plugin github --scope=user\n\nℹ Starting configuration of github for \'user\' scope\n → GitHub default organization [getflox]:\n → Default branch [develop]:\n → Enable vulnerability alerts [Y/n]:\n → Enable automated security fixes [Y/n]:\nℹ \'List of protected branches\' configuration is accepting multiple values, each in new line, enter empty value to end input, \'-\' to delete value\n → List of protected branches [master]:\n → Create repository as private [Y/n]:\n → Enable projects [Y/n]:\n → Enable issue management [Y/n]:\n → Enable wiki [Y/n]:\nℹ \'Collaborators with "pull" permission\' configuration is accepting multiple values, each in new line, enter empty value to end input, \'-\' to delete value\nℹ \'Collaborators with "push" permission\' configuration is accepting multiple values, each in new line, enter empty value to end input, \'-\' to delete value\nℹ \'Collaborators with "admin" permission\' configuration is accepting multiple values, each in new line, enter empty value to end input, \'-\' to delete value\n\nNew configuration:\n\n Key                                    Old value  New value\n─────────────────────────────────────────────────────────────\n Collaborators with "pull" permission   {}         -\n Collaborators with "push" permission   {}         -\n Collaborators with "admin" permission  {}         -\n\nSave plugin settings? [y/N]: y\nℹ Configuration saved: /Users/user/.flox/settings.toml\n → GitHub Access Token [xxx]: ------\n \nNew configuration:\n\n Key                  Old value                                  New value\n──────────────────────────────────────────────────────────────────────────────────────────────────────────\n GitHub Access Token  -----                                      --------\n\nSave plugin settings? [y/N]: y\nℹ Updated 1 secrets\n```\n',
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
