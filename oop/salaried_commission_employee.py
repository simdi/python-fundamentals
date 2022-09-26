# salaried_commission_employee.py
"""SalariedCommissionEmployee class that inherits from CommissionEmployee."""

from decimal import Decimal
from commission_employee import CommissionEmployee

class SalariedCommissionEmployee(CommissionEmployee):
  """A salaried commission employee."""

  def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate, base_salary):
    """Initializes a SalariedCommissionEmployee object."""
    super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)
    self._base_salary = base_salary # validate via property

  @property
  def base_salary(self):
    """Returns the base salary of the employee."""
    return self._base_salary

  @base_salary.setter
  def base_salary(self, salary):
    """Sets the base salary of the employee."""
    if salary < Decimal('0.00'):
      raise ValueError('Base salary must be >= 0')
    self._base_salary = salary

  def earnings(self):
    """Calculates the earnings of the employee."""
    return super().earnings() + self._base_salary

  def __str__(self) -> str:
    return f'{super().__str__()} {self._base_salary:,.2f}'

  def __repr__(self) -> str:
    return f'SalariedCommissionEmployee({super().__repr__()}, {self._base_salary})'
