__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    ManagementFeeStrategy appplies a fixed management fee as per the account balance.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initilizes the ManagementfeeStrategy according to given attributes.
        
        Args:
            date_created: The date when the account created.
            management_fee: A fixed management fee to be applied.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Returns the service charges for calculation.
        
        Args:
            Account(BankAccount): BankAccount receiving service charges.
            
        Returns:
        float: The calculated service charge.
        """
        if self.__date_created <= self.TEN_YEARS_AGO:
            service_charges = self.BASE_SERVICE_CHARGE
        else:
            service_charges = self.BASE_SERVICE_CHARGE + self.__management_fee
        return service_charges
