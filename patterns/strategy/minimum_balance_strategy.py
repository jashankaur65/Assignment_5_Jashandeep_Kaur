__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    The MinimumBalanceStrategy charges a fee depending on whether
    the balance meets the account or exceeds.
    If the balance is above or equal to the threshold, a standard fee applies.
    If it's below, a higher fee is charged.
    """
    SERVICE_CHARGE_PREMIUM: float = 2.0


    def __init__(self, minimum_balance:float):
        """
        Initilizes the MinimumBalanceStrategy according to given attributes.
        
        Args:
            minimum_balance(float): The minimum balance is needed to avoid service charge.
        """
        self.__minimum_balance = minimum_balance
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Returns the service charges for calculation.
        
        Args:
            Account(BankAccount): BankAccount receiving service charges.
            
        Returns:
        float: The calculated service charge.
        """
        if account.balance < self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE
    


