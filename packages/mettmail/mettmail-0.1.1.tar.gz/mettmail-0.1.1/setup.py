# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mettmail']

package_data = \
{'': ['*']}

install_requires = \
['aioimaplib>=0.9.0,<0.10.0',
 'click>=8.0.3,<9.0.0',
 'loguru>=0.5.3,<0.6.0',
 'strictyaml>=1.6.1,<2.0.0']

entry_points = \
{'console_scripts': ['mettmail = mettmail.mettmail_cli:run']}

setup_kwargs = {
    'name': 'mettmail',
    'version': '0.1.1',
    'description': 'Fetch mails from IMAP servers and deliver them to a local user',
    'long_description': '# mettmail\n\nGet mail from IMAP server with IDLE extension and deliver to LMTP server, nothing else.\n\n## Requirements\n\n* python >=3.8\n* [poetry](https://python-poetry.org/) (`pip install --user poetry`)\n\n## Install\n\nInstall mettmail python package and CLI command.\n\n```shell\npoetry install --no-root\n```\n\n## Run\n\nCreate configuration file based on the example:\n\n```shell\ncp mettmail.example.yaml mettmail.yaml\n```\n\nEdit it with your IMAP/LMTP connection details. You can override most of `DeliverLMTP` and `FetchIMAP` constructor parameters.\n\nRun parameters:\n\n```shell\npoetry run mettmail --help\n```\n\n## Development\n\n### Build Dependencies\n\n* [nox](https://nox.thea.codes/) as test-runner\n* [pyenv](https://github.com/pyenv/pyenv) (recommended) to manage python versions\n\nInstall dependencies and pre-commit hooks:\n\n```shell\n# you may need to install the following tools outside of your virtualenv, too:\npip install nox poetry pre-commit\npoetry install --no-root\npoetry run pre-commit install\n```\n\n### Test/Coverage setup\n\n#### Quickly\n\nYou can quickly run tests with:\n\n```shell\n# using your default interpreter\npoetry run pytest\n\n# using nox (add -r for the following runs)\nnox -p 3.8\n```\n\n#### Thoroughly\n\n**Note:** Python 3.10 support is currently broken because of a bug in `aioimaplib`.\n\nUse `nox` to run tests and other useful things automatically for all supported python versions.\n\nInitial setup for all interpreters and environments:\n\n```shell\npyenv install 3.8.12\npyenv install 3.9.9\npyenv install 3.10.1\npyenv local 3.8.12 3.9.9 3.10.1\nnox\n```\n\nAfter that it runs much more quickly reusing the created virtualenvs:\n\n```shell\nnox -r\n```\n',
    'author': 'spezifisch',
    'author_email': 'spezifisch-gpl.7e6@below.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/spezifisch/mettmail',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
