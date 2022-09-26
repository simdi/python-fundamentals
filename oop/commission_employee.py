# commission_employee.py
"""CommissionEmployee base class."""
from decimal import Decimal

# Implicitly inherits from object like all classes in Python 3
# like so: class CommissionEmployee(object):
class CommissionEmployee:
  """An employee who gets paid commission based on gross sales."""

  def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
    """Initializes a CommissionEmployee object."""
    self._first_name = first_name
    self._last_name = last_name
    self._ssn = ssn
    self._gross_sales = gross_sales # validate via property
    self._commission_rate = commission_rate # validate via property

  @property
  def first_name(self):
    """Returns the first name of the employee."""
    return self._first_name

  @property
  def last_name(self):
    """Returns the last name of the employee."""
    return self._last_name

  @property
  def ssn(self):
    """Returns the social security number of the employee."""
    return self._ssn

  @property
  def gross_sales(self):
    """Returns the gross sales of the employee."""
    return self._gross_sales

  @gross_sales.setter
  def gross_sales(self, sales):
    """Sets the gross sales of the employee."""
    if sales < Decimal('0.00'):
      raise ValueError('Gross sales must be >= 0')
    self._gross_sales = sales

  @property
  def commission_rate(self):
    """Returns the commission rate of the employee."""
    return self._commission_rate

  @commission_rate.setter
  def commission_rate(self, commission_rate):
    """Sets the commission rate of the employee."""
    if not 0 < commission_rate < 1:
      raise ValueError('Commission rate must be > 0 and < 1')
    self._commission_rate = commission_rate

  def earnings(self):
    """Calculates the earnings of the employee."""
    return self._gross_sales * self._commission_rate

  def __str__(self):
    """Returns a string representation of the employee."""
    return f'{self._first_name} {self._last_name}: {self._ssn}'

  def __repr__(self):
    """Returns a string representation of the employee."""
    return f'CommissionEmployee({self._first_name}, {self._last_name}, {self._ssn}, {self._gross_sales:.2f}, {self._commission_rate})'

  def __format__(self, format):
    """Returns a formatted string representation of the employee."""
    return f'{str(self):{format}}'
