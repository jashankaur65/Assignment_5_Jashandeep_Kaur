"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import savings_account
from bank_account.savings_account import SavingsAccount
from bank_account.bank_account import BankAccount
from datetime import date
from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount


# 2. Create a Client object with data of your choice.
try:
    client_1 = Client(5689, "Arshdeep","Kaur", "arshdeepdhiman969@gmail.com")
except ValueError as e:
        print(e)
        
        
# 3a. Create a ChequingAccount object with data of your choice,
# using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice,
# using the client_number 
# of the client created in step 2.

try:
    chequing_account_1 = ChequingAccount(78943, 4032, 400.0, date(2025,3,15), 40.2, 0.015)
except ValueError as e:
    print(e)

try:
    savings_account_1 = SavingsAccount(6794, 4032,
                                     400.2, date(2025,3,15), 200.0)
except ValueError as e:
    print(e)
    
# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) 
# to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) 
# to the SavingsAccount object (created in step 2).

chequing_account_1.attach(client_1)
savings_account_1.attach(client_1)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice,
# using the client_number 
# of the client created in this step.
try:
    client_2 = Client(5690, "Samandeep", "Singh", "sdhiman10@gmail.com")
except ValueError as e:
    print(e)

try:
    savings_account_2 = SavingsAccount(270643, 643, 400.2, date(2025,3,15), 320.0)
except ValueError as e:
    print(e)

savings_account_2.attach(client_2)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
print("Client 1 - Chequing account")

try:
     chequing_account_1.deposit(300.0)
     print("Deposit: $300")
except:
     print(e)

try:
     chequing_account_1.deposit(500.0)
     print("Deposit: $500")
except:
     print(e)

try:
     chequing_account_1.withdraw(690.0)
     print("Withdraw: $690")
except:
     print(e)

print("Client 1 - Savings account")

try:
     savings_account_1.deposit(3000.0)
     print("Deposit: $3000.0")
except:
     print(e)

try:
     savings_account_1.deposit(7000.0)
     print("Deposit: $7000")
except:
     print(e)

try:
     savings_account_1.withdraw(800.0)
     print("Withdraw: $800")
except:
     print(e)

print("Client 2 - Savings account")

try:
     savings_account_2.deposit(1000.0)
     print("Deposit: $1000.0")
except:
     print(e)

try:
     savings_account_2.deposit(200.0)
     print("Deposit: $200")
except:
     print(e)

try:
     savings_account_2.withdraw(500.0)
     print("Withdraw: $500")
except:
     print(e)




    
    
