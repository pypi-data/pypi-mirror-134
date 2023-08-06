# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_ccb']

package_data = \
{'': ['*']}

install_requires = \
['attrs', 'pendulum', 'requests']

setup_kwargs = {
    'name': 'python-ccb',
    'version': '1.0.1',
    'description': 'Python wrapper for clearcheckbook',
    'long_description': "Python wrapper for ClearCheckBook\n=================================\n\n[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![builds.sr.ht status](https://builds.sr.ht/~ocurero/python-ccb/.build.yml.svg)](https://builds.sr.ht/~ocurero/python-ccb/.build.yml?) [![readthedocs](https://readthedocs.org/projects/python-ccb/badge/?version=latest&style=flat)](https://python-ccb.readthedocs.io/)\n\nThis package provides a simple python interface for interacting with\nClearCheckBook\n\n* Open Source: Apache 2.0 license.\n* Website: <https://sr.ht/~ocurero/python-ccb/>\n* Documentation: <https://python-ccb.readthedocs.io/>\n\nQuickstart\n----------\n\nUsing **python-ccb** is very simple:\n\n```python\n\n    import python_ccb\n\n    session = python_ccb.ClearCheckBook('user', 'passwd')\n    account = session.get_account('My Account')\n    new_tran = python_ccb.Transaction('Something', 50, python_ccb.WITHDRAW, account=account)\n    session.insert_transaction(new_tran)\n\n```\n\n## What's implemented?\n\n| Feature        | Implemented? |\n| -------------- | ------------ |\n| Accounts       | YES          |\n| Account groups | NO           |\n| Bills          | NO           |\n| Budgets        | NO           |\n| Categories     | YES          |\n| Currencies     | YES          |\n| Object count   | NO           |\n| Premium        | NO           |\n| Transactions   | YES          |\n| Reminders      | NO           |\n| Reports        | NO           |\n\n\n",
    'author': 'Oscar Curero',
    'author_email': 'oscar@curero.es',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://sr.ht/~ocurero/python-ccb/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
