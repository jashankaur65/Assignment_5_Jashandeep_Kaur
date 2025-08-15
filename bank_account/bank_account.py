__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"


from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.observer import Observer
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    """
    It represents BankAccount with different attributes such as
    account number, client number, balance and date created.
    """
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    LOW_BALANCE_LEVEL = 50.0

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date):
        """
        Initializes the BankAccount attributes with argument values.

        Args:
            account_number: An integer value representing the bank account
              number.
            client_number: An integer value representing the client number
              representing the account holder.
            balance: A float value representing the current balance
              of the bank account.
            date_created: A date represents when the bank class is created.
            
        Raises:
            ValueError: if the value of account_number or
              client_number is not an integer.
            ValueError: if the incoming balance cannot be converted to a float,
              the attribute representing the balance should be set to 0.
        """
        super().__init__()
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")
        
        try:
            self.__balance = float(balance)
            if self.__balance < 0:
                raise ValueError("Balance cannot be negative.")
        except ValueError:
            self.__balance = 0.0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()  
          
    @abstractmethod
    def update(self):
        pass
  
    @property
    def account_number(self) -> int:
        """
        Accessor for the BankAccount account number.

        Returns:
            int: An integer value representing the account number.
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for the BankAccount client number.

        Returns:
            int: An integer value representing the client number.
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for the BankAccount balance.

        Returns:
            float: A float value representing the balance.
        """
        return self.__balance
    
    @property
    def date_created(self) -> date:
        """
        Accessor for the BankAccount date created.

        Returns:
            date: A date representing when the account was created.
        """
        return self._date_created

    def _update_balance(self, amount: float):
        """
        Updates the balance by adding the given amount.
          The amount can be negative to reduce the balance.

        Args:
            amount: A float value representing the amount to be
              added to the balance.
    
        Note:
            This method is used by the deposit
            and withdraw methods.
        """
        self.__balance += amount
        
        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:.2f}: on account {self.__account_number}.")
        
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount:.2f}: on account {self.__account_number}.")

    def deposit(self, amount: float):
        """
        Deposits the given amount into the account after validation.
        
        Args:
            amount: A positive numeric value to deposit into the account.
        
        Raises:
            ValueError: If the deposit amount is not numeric or not positive.
        """
        self._update_balance(amount)

    def withdraw(self, amount: float):
        """
        Withdraws the given amount from the account after validation.
        
        Args:
            amount: A positive numeric value to withdraw from the account.
        
        Raises:
            ValueError: If the withdraw amount is not numeric or not positive.
            ValueError: If the withdraw amount exceeds the current balance.
        """
        self._update_balance(-amount)

    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount.
        The balance is formatted with currency symbol and two decimal places.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"
    
    def attach(self, observer: Observer):
        """
        Add an observer to the list.
        """
        self._observers.append(observer)
        
    def detach(self, observer: Observer):
        """
        Remove an observer from the list.  
        """
        self._observers.remove(observer)

    def notify(self, message: str):
        """
        Notify all observers with a message.
        """
        for observer in self._observers:
            observer.update(message)
            
  
                    

