__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """InvestmentAccount is meant for clients with a long-term savings plan."""


    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created, management_fee: float):
        """
        Initializes the InvestmentAccount class with the specified arguments.
        
        Args:
            account_number: An integer representing the account number.
            client_number: An integer representing the client number.
            balance: A float representing the balance of the account.
            date_created: A date representing when the account was created.
            management_fee: A float representing the management fee charged
            by the bank.
        
        Raises:
            ValueError: If management_fee cannot be converted to a float.
        """

        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        try:
            self.__management_fee = float(management_fee)          
        except :
            self.__management_fee = 2.55  
        
        self.__strategy = ManagementFeeStrategy(self._date_created,
                                            self.__management_fee)
    def update(self):
        pass
       
    def __str__(self):
        """
        Returns a string representation of the InvestmentAccount.
        
        If the account is more than 10 years old, the management fee is waived.
        """
        base_str = super().__str__()
        if self._date_created > self.TEN_YEARS_AGO:
            fee_str = f"Management Fee: ${self.__management_fee:,.2f}%" 
        else:
            fee_str = "Management Fee: Waived"

        return f"{base_str}\nDate Created: {self._date_created} {fee_str} Account Type: Investment"
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charges for the investment account.
        ManagementFeeStrategy is used to calculate service charges based on
        when the account was created and its management fee.
        
        Returns:
        float: The total service charge for the investment account.
        """
        return self.__strategy.calculate_service_charges(self)

       
    
