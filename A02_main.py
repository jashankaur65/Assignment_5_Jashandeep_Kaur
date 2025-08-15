"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

# 1.  Import all BankAccount types using the bank_account package
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(34567, 7891, 300.00, date.today(), 60.00, 0.7)

print("===================================================")
# 3. Print the ChequingAccount created in step 2.
print("Chequing Account:") 
print (chequing_account)
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_account.get_service_charges():.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(500.00)
# 4b. Print the ChequingAccount
print("\nChequing Account after deposit:", chequing_account)
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_account.get_service_charges():.2f}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(34567, 7891, 300.00, date.today(), 60.00)

# 6. Print the SavingsAccount created in step 5.
print("Savings Account:") 
print(savings_account)

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_account.get_service_charges():.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings_account.withdraw(60.00)
# 7b. Print the SavingsAccount.
print("\nSavings Account:") 
print (savings_account)
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_account.get_service_charges():.2f}")


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account = InvestmentAccount(4591, 4592, 400.00, date(2024, 8, 13), 6)

# 9a. Print the InvestmentAccount created in step 8.
print("Investment Account:\n", investment_account)
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(f"Service Charges: ${investment_account.get_service_charges():.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account = InvestmentAccount(4591, 4592, 400.00, date(2015, 6, 1), 13)

# 11a. Print the InvestmentAccount created in step 10.
print("\nInvestment Account:")
print(investment_account)
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(f"Service Charges: ${investment_account.get_service_charges():.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
chequing_account.withdraw(chequing_account.get_service_charges())
savings_account.withdraw(savings_account.get_service_charges())
investment_account.withdraw(investment_account.get_service_charges())
investment_account.withdraw(investment_account.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print("Account Status:")
print("\nChequing Account:") 
print(chequing_account)
print("\nSavings Account:")
print(savings_account)
print("\nNew Investment Account:")
print(investment_account)
print("\nOld Investment Account:")
print(investment_account)
print(" ")
