__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"


from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import date
class Client(Observer):
    """
    client class: It represents a client with attributes such as
      client number, first name, last name and email address.
    """

    def __init__(self, client_number: int, first_name: str,
                  last_name: str, email_address: str):
        """
        Initializes the class attributes with argument values.
           
        Args:
            client_number (int): An integer value representing
                the client number.
            first_name (str):The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.
        Raises:
            ValueError: if the client number is not an positive integer.
            ValueError: if the first or last name is blank.
            EmailNotValidError: if the email address is invalid.
        """
        
        if isinstance(client_number, int) and client_number > 0:
            self.__client_number = client_number
        else:
            raise ValueError("client_number must be a positive integer.")
        
        if len(first_name) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("first_name cannot be blank.")
        
        if len(last_name) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("last_name cannot be blank.")
        
        try:
            validated_email = validate_email(email_address, 
                                             check_deliverability = False)  
            self.__email_address = validated_email.normalized
        except EmailNotValidError:
            raise EmailNotValidError(f"Invalid email address: {email_address}")
           
        
    @property
    def client_number(self) -> int:
        """
        Accessor for the client attribute.

        Returns:
            int: An integer value representing the client number.
        """
        return self.__client_number
        
    @ property
    def first_name(self) -> str:
        """
        Accessor for the first_name attribute.

        Returns:
            str: A string value the client's first name.
        """
        return self.__first_name
        
    @ property
    def last_name(self) -> str:
        """
        Accessor for the last_name attribute.

        Returns:
            str: A string value the client's last name.
        """
        return self.__last_name
        
    @ property 
    def email_address(self) -> str:
        """
        Accessor for the email_address attribute.

        Returns:
            str: A string value the client's email address.
        """
        return self.__email_address
        
    def __str__(self) -> str:
        """
        Returns a string representation of client object.

        Returns:
            str: A string representing the client's last name, first name,
              client number, and email address.
        """
        return (f"{self.last_name}, "
                + f"{self.first_name},"
                + f"[{self.client_number}] - {self.email_address}"
        )
        
    def update(self, message:str):
        subject = f"ALERT: Unusual Activity: {date.today()}"
        email_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        simulate_send_email(self.email_address, subject, email_message)


