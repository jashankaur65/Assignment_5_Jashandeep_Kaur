__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Abstract class which helps to define strategy for service charges.
    """
    BASE_SERVICE_CHARGE: float = 0.50
    
    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract Method used to calculate service charge according to
        given balance.
        """
        pass 
    