""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"


from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.


    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client = Client(12345, "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
        print("Client instance created successfully.")
    except ValueError as e:
        print(f"Error creating Client instance: {e}")


    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

 

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    try:
        bank_account = BankAccount(12345, client.client_number, 100.00)
    except ValueError as e:
        print(f"Error creating BankAccount: {e}")



    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    try:
        invalid_balance = BankAccount(12346, client.client_number, "INVALID")
    except ValueError as e:
        print(f"Error creating BankAccount with invalid balance: {e}")


    # 5. Code a statement which prints the Client instance created in step 1.
    print(f"Client: {client}")


    # Code a statement which prints the BankAccount instance created in step 3.
    print(f"Bank Account: {bank_account}")


    # 6. Attempt to deposit a non-numeric value into the BankAccount
    #  create in step 3. 
    try:
        bank_account.deposit("invalid_amount")
    except ValueError as e:
        print(f"Error depositing amount: {e}")

    # 7. Attempt to deposit a negative value into the BankAccount
    #  create in step 3. 
    try:
        bank_account.deposit(-20.0)
    except ValueError as e:
        print(f"Error depositing negative amount: {e}")


    # 8. Attempt to withdraw a valid amount of your choice from the
    #  BankAccount create in step 3. 
    try:
        bank_account.withdraw(30.0)
        print(f"Withdrawal successful, new balance: {bank_account.balance}")
    except ValueError as e:
        print(f"Error withdrawing amount: {e}")


    # 9. Attempt to withdraw a non-numeric value from the BankAccount
    #  create in step 3. 
    try:
        bank_account.withdraw("invalid_amount")
    except ValueError as e:
        print(f"Error withdrawing amount: {e}")



    # 10. Attempt to withdraw a negative value from the BankAccount
    #  create in step 3. 
    try:
        bank_account.withdraw(-50.0)
    except ValueError as e:
        print(f"Error withdrawing negative amount: {e}")

    # 11. Attempt to withdraw a value from the BankAccount
    #  create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        bank_account.withdraw(200.0)
    except ValueError as e:
        print(f"Error withdrawing amount greater than balance: {e}")  

    # 12. Code a statement which prints the BankAccount instance
    #  created in step 3.
    print(f"Final Bank Account: {bank_account}")



if __name__ == "__main__":
    main()