Python wrapper for ClearCheckBook
=================================

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![builds.sr.ht status](https://builds.sr.ht/~ocurero/python-ccb/.build.yml.svg)](https://builds.sr.ht/~ocurero/python-ccb/.build.yml?) [![readthedocs](https://readthedocs.org/projects/python-ccb/badge/?version=latest&style=flat)](https://python-ccb.readthedocs.io/)

This package provides a simple python interface for interacting with
ClearCheckBook

* Open Source: Apache 2.0 license.
* Website: <https://sr.ht/~ocurero/python-ccb/>
* Documentation: <https://python-ccb.readthedocs.io/>

Quickstart
----------

Using **python-ccb** is very simple:

```python

    import python_ccb

    session = python_ccb.ClearCheckBook('user', 'passwd')
    account = session.get_account('My Account')
    new_tran = python_ccb.Transaction('Something', 50, python_ccb.WITHDRAW, account=account)
    session.insert_transaction(new_tran)

```

## What's implemented?

| Feature        | Implemented? |
| -------------- | ------------ |
| Accounts       | YES          |
| Account groups | NO           |
| Bills          | NO           |
| Budgets        | NO           |
| Categories     | YES          |
| Currencies     | YES          |
| Object count   | NO           |
| Premium        | NO           |
| Transactions   | YES          |
| Reminders      | NO           |
| Reports        | NO           |


