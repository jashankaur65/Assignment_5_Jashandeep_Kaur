__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from datetime import date 
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    A ChequingAccount is meant for banking client who has frequent transactions of both deposits and withdraws.
    """

    def __init__(self, account_number: int,
                  client_number: int,
                    balance: float,
                    date_created: date,
                    overdraft_limit: float,
                    overdraft_rate: float):
        """
        initilizes the chequing class with argument values.

        Args:
            account_number: An interger value representing the bank account
              number.
            client_number: An integer value representing the client number
              representing the account holder.
            balance: A float value representing the current balance
              of the bank account.
            date_created: A date represents when the bank class is created.
            overdraft_limit: The maximum amount that a balance can be overdrawn(below 0.0) before overdraft fees are applied.
            overdraft_rate: The rate to which the overdraft fees will be applied.
               
        Raises:
            ValueError: if the value of account_number or
              client_number is not an integer.
            ValueError: if the incoming balance cannot be converted to a float,
              the attribute representing the balance should be set to 0.
        """

        super().__init__(account_number, client_number,
                         balance, date_created)
        
        if isinstance(overdraft_limit, float):
            self.__overdraft_limit = overdraft_limit
        else:
            self.__overdraft_limit = -100.00

        if isinstance(overdraft_rate, float):
            self.__overdraft_rate = overdraft_rate
        else:
            self.__overdraft_rate = 0.5
          
        self.__strategy = OverdraftStrategy(self.__overdraft_limit,
                                            self.__overdraft_rate)

    def __str__(self) -> str:
      """
      Returns a string representation of the ChequingAccount,
      including its overdraft information.
      """
      return_value = super().__str__()
      return_value += f"\nOverdraft Limit: ${self.__overdraft_limit:.2f} "
      return_value += f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
      return_value += "Account Type: Chequing"
      
      return return_value.strip()

    def get_service_charges(self) -> float:
      """
      Calculates and returns the service charge for the current account based on 
      service charge strategy.

      Returns: 
        The calculated service charges as a float.
      """
      return self.__strategy.calculate_service_charges(self)
 
    def update(self):
        print("Updating chequing account")