# account.py
"""Account class definition."""
from decimal import Decimal

class Account:
    """
      Account class for maintaining a bank account balance.
      Attributes:
        name: The name of the account holder.
        balance: The current balance of the account.
    """

    def __init__(self, name, balance):
        """Initialize the Account object."""
        # If balance is less than 0, raise an exception
        if balance < Decimal("0.00"):
          raise ValueError("Initial balance must be >= 0.00")

        self._name = name
        self._balance = balance

    def __str__(self):
        """Return a string representation of the Account object."""
        return f"Account: {self._name}, Balance: {self._balance}"

    def deposit(self, amount):
        """Deposit the amount into the account."""
        if amount < Decimal("0.00"):
          raise ValueError("Amount must be >= 0.00")
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw the amount from the account."""
        if amount < Decimal("0.00"):
          raise ValueError("Amount must be >= 0.00")

        if self._balance < amount:
          raise ValueError("Insufficient funds")

        self._balance -= amount

    def get_balance(self):
        """Return the balance of the account."""
        return self._balance

    def get_name(self):
        """Return the account number."""
        return self._name

    def transfer(self, amount, account):
        """Transfer the amount to the account."""
        if amount < Decimal("0.00"):
          raise ValueError("Amount must be >= 0.00")

        if self._balance < amount:
          raise ValueError("Insufficient funds")

        self.withdraw(amount)
        account.deposit(amount)

    def get_account_type(self):
        """Return the account type."""
        return "Account"