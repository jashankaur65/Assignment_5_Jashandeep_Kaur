__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy. minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.0   

    def __init__(self, account_number: int, client_number: int, balance: float, 
                 date_created: date, minimum_balance: float):
        """
        Initializes a SavingsAccount instance with the given attributes.
        Inherits from the BankAccount class.

        Args:
        account_number: The account number of the Savings Account
        client_number: The client number
        balance: The current balance of the Savings Account
        date_created: The creation date of the Savings Account
        minimum_balance: The minimum balance before service charges are applied
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0 
        
        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def get_service_charges(self) -> float:
       """
       Based on the given strategy, service chage for account will be returned.
       
       Returns:
            The calculated service charge as a float.
       """
       return self.__strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the SavingsAccount.
        Uses the super class __str__ method and includes minimum_balance.
        """
        return (super().__str__() +
                f"\nMinimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings")
        
    def update(self, message: str):
            """Handles notifications received from the Subject."""
            print(f"Notification for Savings Account {self.account_number}: {message}")
