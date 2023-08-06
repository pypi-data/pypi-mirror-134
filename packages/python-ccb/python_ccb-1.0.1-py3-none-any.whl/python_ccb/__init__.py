from base64 import b64encode
from functools import lru_cache
from urllib.parse import urljoin
from attrs import define, field
import pendulum
import requests


def _make_constant(const_name, const_value):
    class Constant:
        value = const_value

        def __repr__(self):
            return self.__name__

    constant = Constant()
    constant.__name__ = const_name
    constant.__qualname__ = const_name
    return constant


WITHDRAW = _make_constant('WITHDRAW', 0)
"""Constant for withdraw transactions"""
DEPOSIT = _make_constant('DEPOSIT', 1)
"""Constant for deposit transactions"""
TRANSFER = _make_constant('TRANSFER', 2)
"""Constant for transfer transactions"""
CASH = _make_constant('CASH', 1)
"""Constant for cash accounts"""
CHECKING = _make_constant('CHECKING', 2)
"""Constant for checking accounts"""
SAVINGS = _make_constant('SAVINGS', 3)
"""Constant for saving accounts"""
CREDIT = _make_constant('CREDIT', 4)
"""Constant for credit card accounts"""
INVESTMENT = _make_constant('INVESTMENT', 5)
"""Constant for investment accounts"""


class _ClearCheckBookSession(requests.Session):

    api_version = '2.5'
    prefix_url = f'https://www.clearcheckbook.com/api/{api_version}/'

    def __init__(self, app_ref):
        self.app_ref = app_ref
        super().__init__()

    def request(self, method, url, *args, **kwargs):
        kwargs['params'] = {**kwargs.get('params', {}), **{'app_ref': self.app_ref}}
        kwargs['data'] = {**kwargs.get('data', {}), **{'app_ref': self.app_ref}}
        url = urljoin(self.prefix_url, url)
        return super().request(method, url, *args, **kwargs)


class ClearCheckBook:
    """This class connects to ClearCheckBook

    Args:
        username (str): Username used to login to ClearCheckBook
        password (str): Password used to login to ClearCheckBook
        app_ref (str): Application tracking ID. Defaults to None.
    """

    def __init__(self, username, password, app_ref='python-ccb'):

        self._session = _ClearCheckBookSession(app_ref)
        self._session.auth = (b64encode(username.encode('latin1')),
                              b64encode(password.encode('latin1')))

    def get_accounts(self, is_overview=False, all=True):
        """Get all accounts.

        Args:
            is_overview (bool): `True` to return only the accounts with a balance. `False`
                to return every account. Defaults to `False`
            all (bool): `True` to return all accounts and `NO_ACCOUNT` if it exists.

        Returns:
            A list of `Account`

        """
        response = self._session.get('accounts', params={'is_overview': is_overview,
                                                         'all': all})
        response.raise_for_status()
        if not response.json()['status']:
            raise RuntimeError(response.json()['error_msg'])
        return [Account.from_api(account_data,
                                 self.get_currency(account_data['currency_code']))
                for account_data in response.json()['data']]

    def get_account(self, name=None, account_id=None):
        """Get an account.

        Args:
            name (str): name of the account
            account_id (int): id of the account

        Returns:
            `Account`

        Warning:
            ClearCheckBook lets you add two accounts with the same name. In this case
            API behavior is unpredictable.
        """

        if account_id == 0:
            return NO_ACCOUNT
        elif name:
            for account in self.get_accounts():
                if account.name == name:
                    return account
            else:
                raise ValueError(f'no account found with name {name}')
        else:
            response = self._session.get('account', params={'id': account_id})
            response.raise_for_status()
            if not response.json()['status']:
                raise RuntimeError(response.json()['error_msg'])
            account_data = response.json()['data']
            return Account.from_api(account_data,
                                    self.get_currency(account_data['currency_code']))

    def get_transaction(self, id):
        """Get a transaction.

        Args:
            id (int): ID of the transaction

        Returns:
            `Transaction`
        """

        response = self._session.get('transaction', params={'id': id})
        response.raise_for_status()
        if not response.json()['status']:
            raise RuntimeError(response.json()['error_msg'])
        tr_data = response.json()['data']
        return Transaction.from_api(tr_data,
                                    self.get_account(account_id=tr_data['account_id']),
                                    self.get_category(category_id=tr_data['category_id']),
                                    self.get_transaction(tr_data['parent']) if
                                    tr_data['parent'] else None)

    def get_transactions(self, account=None, created_at=None, from_trans=None,
                         order=None, order_direction=None, separate_splitsid=None):
        """Get all transactions. This method returns an `Transaction` interator.

        Args:
            account (Account): Account to get transactions from. Defaults to all accounts.
            created_at (pendulum.Datetime): Start timestamp to retrieve transactions from.
                Defaults to all transactions.
            from_trans (Transaction): Retrieve all transactions added after this
                transaction.
            order (str): Which column to sort the transactions on: date, created_at,
                amount, account, category, description, memo, payee, check_num.
            order_direction: Whether to return the results in ascending or descending
                order. Valid parameters are DESC or ASC.
            separate_splitsid (bool): Whether to have splits appear in order under their
                parents. If you're trying to retrieve newly added transactions, set this to
                `True` or else split children will inherit the parent's `created_at` value
        Returns:
            Iterator
        """

        limit = 250
        page = 1
        accounts = {account.id: account for account in self.get_accounts()}
        categories = {category.id: category for category in self.get_categories()}
        while True:
            params = {'account_id': account.id if account else None,
                      'created_at': created_at.to_date_string() if created_at else None,
                      'from_id': from_trans.id if from_trans else None,
                      'created_at_time': created_at.to_time_string()
                      if created_at else None,
                      'created_at_timezone':  created_at.timezone if created_at else None,
                      'order': order,
                      'order_direction': order_direction,
                      'separate_splitsid': separate_splitsid,
                      'limit': limit,
                      'page': page}
            response = self._session.get('transactions', params=params)
            response.raise_for_status()
            if not response.json()['status']:
                raise RuntimeError(response.json()['error_msg'])
            if not response.json()['data']:
                break
            for tr_data in response.json()['data']:
                yield Transaction.from_api(tr_data,
                                           accounts.get(tr_data['account_id'],
                                                        NO_ACCOUNT),
                                           categories.get(tr_data['category_id'],
                                                          NO_CATEGORY),
                                           self.get_transaction(tr_data['parent']) if
                                           tr_data['parent'] else None)
            page += 1

    def _manage_transaction(self, method, transaction, data, from_account,
                            to_account, is_split, split_amounts, split_categories,
                            split_descriptions):
        data['date'] = transaction.date.to_date_string() if transaction.date else None
        data['amount'] = transaction.amount
        data['transaction_type'] = transaction.type.value
        data['account_id'] = transaction.account.id
        data['category_id'] = transaction.category.id
        data['description'] = transaction.description
        data['jive'] = 1 if transaction.jive else 0
        data['from_account_id'] = from_account.id if from_account else None
        data['to_account_id'] = to_account.id if to_account else None
        data['check_num'] = transaction.check_num
        data['memo'] = transaction.memo
        data['payee'] = transaction.payee
        data['is_split'] = 'true' if is_split else 'false'
        data['split_amounts[]'] = split_amounts
        data['split_categories[]'] = split_categories
        data['split_descriptions[]'] = split_descriptions
        response = getattr(self._session, method)('transaction', data=data)
        response.raise_for_status()

        if not response.json()['status']:
            raise RuntimeError(response.json()['error_msg'])
        return [self.get_transaction(tr_id) for tr_id in response.json()['ids']]

    def edit_transaction(self, transaction, from_account=None, to_account=None,
                         is_split=False, split_amounts=[], split_categories=[],
                         split_descriptions=[]):
        """Edit a transaction

        Args:
            transaction (transaction): Transaction to edit.
            from_account (Account): If this transaction is converted into a transfer,
                this is the account you're transferring from.
            to_account (Account): If this transaction is converted into a transfer,
                this is the account you're transferring to.
            is_split (bool): If the transaction is being split, set this to `True`.
            split_amount (list): List of float values for each split child.
            split_categories (list): List of categories for each split child.
            split_descriptions (list): List of descriptions for each split child.

        Returns:
            List of `Transaction`

        Raises:
            ValueError: if transaction doesn't have a valid `id`
        """

        if not transaction.id:
            raise ValueError(f'transaction has no id')
        data = {'id': transaction.id}
        return self._manage_transaction('put', transaction, data, from_account,
                                        to_account, is_split, split_amounts,
                                        split_categories, split_descriptions)

    def insert_transaction(self, transaction, from_account=None, to_account=None,
                           is_split=False, split_amounts=[], split_categories=[],
                           split_descriptions=[]):
        """Insert a transaction

        Args:
            transaction (transaction): Transaction to insert.
            from_account (Account): If this transaction is converted into a transfer,
                this is the account you're transferring from.
            to_account (Account): If this transaction is converted into a transfer,
                this is the account you're transferring to.
            is_split (bool): If the transaction is being split, set this to `True`.
            split_amount (list): List of float values for each split child.
            split_categories (list): List of categories for each split child.
            split_descriptions (list): List of descriptions for each split child.

        Returns:
            List of `Transaction`
        """

        data = {}
        return self._manage_transaction('post', transaction, data, from_account,
                                        to_account, is_split, split_amounts,
                                        split_categories, split_descriptions)

    def delete_transaction(self, transaction):
        """Delete a transaction

        Args:
            transaction (transaction): Transaction to delete.
        """
        response = self._session.delete('transaction', data={'id': transaction.id})
        response.raise_for_status()
        if not response.json()['status']:
            raise RuntimeError(response.json()['error_msg'])

    def transform_transfer(self, transaction, from_account_name, to_account_name):
        """Transform a withdrawal or deposit transactions into a transfer

        Args:
            transaction (transaction): Transaction to transform.
            from_account_name (str): The account you're transferring from.
            to_account_name (str): The account you're transferring to.

        Returns:
            List of `Transaction`

        Warning:
            ClearCheckBook lets you add two accounts with the same name. In this case
            API behavior is unpredictable.
        """

        accounts = self.get_accounts()
        try:
            from_account = accounts[from_account_name]
        except KeyError:
            raise ValueError(f'no account found with name {from_account_name}')
        try:
            to_account = accounts[to_account_name]
        except KeyError:
            raise ValueError(f'no account found with name {to_account_name}')
        transaction.transaction_type = TRANSFER
        return self.edit_transaction(transaction,
                                     from_account=from_account, to_account=to_account)

    def _manage_split(self, method, transaction, split_list):
        split_amounts = []
        split_categories = []
        split_descriptions = []
        for trans_split in split_list:
            split_amounts.append(trans_split.amount)
            split_categories.append(trans_split.category_id)
            split_descriptions.append(trans_split.description)
        transaction.transaction_type = TRANSFER
        return getattr(self, f'{method}_transaction')(transaction,
                                                      split_amounts=split_amounts,
                                                      split_categories=split_categories,
                                                      split_descriptions=split_descriptions
                                                      )

    def insert_split(self, transaction, split_list):
        """Insert a transaction with its splited transactions

        Args:
            transaction (transaction): Transaction to insert.
            split_list (list): Transaction list containing the splitted transactions

        Returns:
            List of `Transaction`
        """

        return self._manage_split('insert', transaction, split_list)

    def edit_split(self, transaction, split_list):
        """Edit a transaction and its splited transactions

        Args:
            transaction (transaction): Transaction to edit.
            split_list (list): Transaction list containing the splitted transactions

        Returns:
            List of `Transaction`
        """

        return self._manage_split('edit', transaction, split_list)

    def get_categories(self):
        """Get all categories

        Returns:
            List of `Castegory`
        """

        response = self._session.get('categories')
        response.raise_for_status()
        if not response.json()['status']:
            raise RuntimeError(response.json()['error_msg'])
        categories = []
        for category_data in response.json()['data']:
            category = Category(**category_data)
            if category.parent:
                for category_parent in categories:
                    if category_parent.id == category.parent:
                        category.parent = category_parent
                        break
            categories.append(category)
        return categories

    def get_category(self, name=None, category_id=None):
        """Get a category

        Args:
            name (str): name of the category
            category_id (int): id of the category

        Returns:
            `Category`

        Warning:
            ClearCheckBook lets you add two categories with the same name. In this case
            API behavior is unpredictable.
         """

        if category_id == 0:
            return NO_CATEGORY
        for category in self.get_categories():
            if category.name == name or category.id == category_id:
                return category
        else:
            raise ValueError(f'no account found with name {name} or id {category_id}')

    @lru_cache(maxsize=16)
    def get_currency(self, code=None, id=None):
        """Get a currency

        Args:
            code (str): The three digit currency code (eg: USD)
            category_id (int): id of the currency

        Returns:
            `Currency`
         """

        if not id and not code:
            raise TypeError('get_currency() takes either the id or code arguments')
        response = self._session.get('currency', params={'code': code, 'id': id})
        response.raise_for_status()
        if not response.json()['status']:
            raise RuntimeError(response.json()['error_msg'])
        return Currency(**response.json()['data'])

    @lru_cache(maxsize=16)
    def get_currencies(self):
        """Get all currencies

        Returns:
            List of `Currency`
         """

        response = self._session.get('currencies')
        response.raise_for_status()
        if not response.json()['status']:
            raise RuntimeError(response.json()['error_msg'])
        return [Currency(**currency) for currency in response.json()['data']]


def _conv_date(date):
    if date and not isinstance(date, pendulum.Date):
        return pendulum.from_format(date, 'YYYY-MM-DD')
    else:
        return date


@define
class Account:
    """ Account object holds account information

    Attributes:
        name (str): Account name
        type (obj): One of [WITHDRAW](#WITHDRAW), DEPOSIT or TRANSFER.
        group_id (int): ID of the account group.
        credit_limit (float): If this is a credit card and the user has entered.
            a credit limit, this value will be returned.
        deposit (float): The float value containing the amount of deposits in this account.
        jive_deposit (float): The float value containing the amount of jived deposits in
            this account.
        withdraw (float): The float value containing the amount of withdrawals in this
            account.
        jive_withdrawal (float): The float value containing the amount of jived withdrawals
            in this account.
        converted_balance (float): The converted balance if this account currency differs
            from their global currency.
        converted_jived (float): the converted jived balance if this account currency
            differs from their global currency.
        unconverted_balance (float): the balance of this account in its native currency.
        unconverted_jived (float): the jived balance of this account in its native
            currency.
        currency (Currency): The currency for this account.
        id (int): The account id.
    """
    name: str
    type: str = field(eq=False, default=None, repr=False)
    group_id: int = field(eq=False, default=None, repr=False)
    credit_limit: float = field(eq=False, default=None, repr=False)
    deposit: float = field(eq=False, default=None, repr=False)
    jive_deposit: float = field(eq=False, default=None, repr=False)
    withdrawal: float = field(eq=False, default=None, repr=False)
    jive_withdrawal: float = field(eq=False, default=None, repr=False)
    converted_balance: float = field(eq=False, default=None, repr=False)
    converted_jived: float = field(eq=False, default=None, repr=False)
    unconverted_balance: float = field(eq=False, default=None)
    unconverted_jived: float = field(eq=False, default=None)
    currency: str = field(eq=False, default=None)
    id: str = field(default=None, repr=False)

    @type.validator
    def _check_type(self, attribute, value):
        if self.id != 0 and value not in (CASH, CHECKING, SAVINGS, CREDIT, INVESTMENT):
            raise ValueError(f'{value} is not a valid account type')

    @classmethod
    def from_api(cls, api_data, currency):
        account_type = {CASH.value: CASH,
                        CHECKING.value: CHECKING,
                        SAVINGS.value: SAVINGS,
                        CREDIT.value: CREDIT,
                        INVESTMENT.value: INVESTMENT
                        }.get(api_data['type_id'])

        return cls(name=api_data['name'],
                   type=account_type,
                   group_id=api_data['group_id'],
                   credit_limit=api_data['credit_limit'],
                   deposit=api_data['deposit'],
                   jive_deposit=api_data['jive_deposit'],
                   withdrawal=api_data['withdrawal'],
                   jive_withdrawal=api_data['jive_withdrawal'],
                   converted_balance=api_data['converted_balance'],
                   converted_jived=api_data['converted_jived'],
                   unconverted_balance=api_data['unconverted_balance'],
                   unconverted_jived=api_data['unconverted_jived'],
                   currency=currency,
                   id=api_data['id'])


NO_ACCOUNT = Account('No Account', id=0)


@define
class Category:
    """ Category object holds category information

    Attributes:
        name (str): Category name.
        parent (Category): If this is a child category, its category parent. None instead.
        id (int): The category ID.
    """
    name: str
    parent: int = field(eq=False, default=None)
    id: int = field(default=None, repr=False)


NO_CATEGORY = Category('No Category', id=0)


@define
class Currency:
    """Currency object holds category information

    Attributes:
        currency_code (str): The three digit currency code (eg: USD)
        text (str): Full name of the currency, with code. (eg: United States Dollar (USD))
        code (str): The HTML character code for the specified currency symbol. (eg: &#36; =
            $)
        format (str): How the currency should be formatted with thousands and decimal
            separators. (eg: #,###.## for USD)
        rate (float): The latest exchange rate to 1 USD
        importance (int): For ordering the list of currencies in a drop down list. 5 = most
            used and should be at the top of the list.
    """
    currency_code: str
    text: str = field(eq=False, default=None)
    code: str = field(eq=False, default=None, repr=False)
    format: str = field(eq=False, default=None, repr=False)
    rate: float = field(eq=False, default=None, repr=False)
    importance: int = field(eq=False, default=None, repr=False)
    id: int = field(default=None, repr=False)


@define(order=True)
class Transaction:
    """Transaction object holds transaction information

    Attributes:
        description (str): The description for this transaction.
        date (pendulum.Datetime):  The date for the transaction.
        amount (float): The amount of the transaction.
        type (Object): One of WITHDRAW, DEPOSIT or TRANSFER.
        account (Account): The account associated with this transaction.
        category (Category): The category associated with this transaction.
        jive (bool): Whether or not this transaction is jived
        specialstatus (str): Text that is empty or says "Transfer" or "Split".
        parent (Transaction):  If this is a split from a split transaction, this is the
            parent transaction.
        related_transfer (str): A unique string corresponding to its related transfer.
        check_num (str): Text from the check number field
        memo (str): Text from the memo field
        payee (str): Text from the payee field
        initial_balance (bool): Boolean for whether or not this was set up as an initial
            balance for an account.
        attachment (str): If a file attachment exists, this is the URL to view it.
    """
 
    description: str = field(eq=False)
    amount: float = field(eq=False)
    type: int = field(eq=False)
    date: pendulum.DateTime = field(converter=_conv_date, default=None, order=True)
    account: Account = field(eq=False, default=NO_ACCOUNT, repr=False)
    category: Category = field(eq=False, default=NO_CATEGORY, repr=False)
    jive: bool = field(eq=False, default=False, repr=False)
    specialstatus: int = field(eq=False, default=None, repr=False)
    parent: object = field(eq=False, default=None, repr=False)
    related_transfer: int = field(eq=False, default=None, repr=False)
    check_num: int = field(eq=False, default=None, repr=False)
    memo: int = field(eq=False, default=None, repr=False)
    payee: int = field(eq=False, default=None, repr=False)
    initial_balance: int = field(eq=False, default=None, repr=False)
    attachment: str = field(eq=False, default=None, repr=False)
    created_at: pendulum.DateTime = field(eq=False, default=None, repr=False)
    id: int = field(default=None, repr=False)

    @type.validator
    def _check_type(self, attribute, value):
        if value is not WITHDRAW and value is not DEPOSIT and value is not TRANSFER:
            raise ValueError(f'{value} is not a valid transaction type')

    @classmethod
    def from_api(cls, api_data, account, category, parent):
        type = (WITHDRAW if api_data['transaction_type'] == WITHDRAW.value else
                DEPOSIT if api_data['transaction_type'] == DEPOSIT.value else TRANSFER)
        try:
            created_at = pendulum.from_format(api_data['created_at'],
                                              'YYYY-MM-DD HH:mm:ss.SSSSSS')
        except ValueError:  # This is needed b/c plaid uses a different format
            created_at = pendulum.from_format(api_data['created_at'],
                                              'YYYY-MM-DD HH:mm:ss')
        return cls(description=api_data['description'],
                   amount=api_data['amount'],
                   type=type,
                   date=pendulum.from_format(api_data['date'], 'YYYY-MM-DD HH:mm:ss'),
                   created_at=created_at,
                   account=account,
                   category=category,
                   jive=True if api_data['jive'] == 'true' else False,
                   specialstatus=api_data['specialstatus'],
                   parent=parent,
                   related_transfer=api_data['related_transfer'],
                   check_num=api_data['check_num'],
                   memo=api_data['memo'],
                   payee=api_data['payee'],
                   initial_balance=api_data['initial_balance'],
                   attachment=api_data['attachment'],
                   id=api_data['id'])
