__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Overdraft class is inherited from ServiceChargeStrategy class which helps to
    calculate service charge when balance of account goes to overdraft. 
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initilizes the overdraft strategy with the given attributes.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate service charge according to account's balance and overdraft limit.
        If the balance is greater than or equal to overdraft limit, the base service charge is applied.
        Else, additional charges will apply on overdraft rate.
        
        Args:
            Account(BankAccount): BankAccount receiving service charges.
            
        Returns:
        float: The calculated service charge.
        
        """
        if account.balance >= self.__overdraft_limit:
            calculated_service = self.BASE_SERVICE_CHARGE
        else:
            calculated_service = self.BASE_SERVICE_CHARGE + \
            (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        
        return calculated_service