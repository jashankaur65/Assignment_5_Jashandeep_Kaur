__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

import os
import sys
import csv
import logging
from datetime import datetime
from bank_account.chequing_account import ChequingAccount
from client.client import Client
from bank_account.bank_account import BankAccount
from patterns.strategy import management_fee_strategy
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount

# Ensure proper path resolution for module imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# *******************************************************************************
# LOGGING SETUP

# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))

# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
os.makedirs(log_dir, exist_ok=True)  

# Log file path
log_file_path = os.path.join(log_dir, 'manage_data.log')

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# *******************************************************************************
# FILE PATH SETUP

data_dir = os.path.join(root_dir, 'data')
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')

# *******************************************************************************

def load_data() -> tuple[dict, dict]:
    """
    Reads client and account data from CSV files and stores them in dictionaries.

    Returns:
        tuple: (client_listing, accounts)
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                client_number = int(record['client_number'])
                first_name = record['first_name'].strip()
                last_name = record['last_name'].strip()
                email_address = record['email_address'].strip()

                if not first_name:
                    raise ValueError(f"First name cannot be blank.")

                client = Client(client_number, first_name, last_name, email_address)
                client_listing[client.client_number] = client
            except Exception as e:
                logging.error(f"Unable to create client: {e}")

    # READ ACCOUNT DATA
        with open(accounts_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for record in reader:
                try:
                    account_number = int(record['account_number'])
                    client_number = int(record['client_number'])
                    balance = float(record['balance'])
                    account_type = record['account_type'].strip()
                    date_created = datetime.strptime(record["date_created"], "%Y-%m-%d").date()
                    
                    # Ensure client exists
                    if client_number not in client_listing:
                        raise ValueError(f"Bank Account {account_number} has an invalid Client Number: {client_number}")

                    # Create the correct account type (future support for subclasses)
                    if account_type == "ChequingAccount":
                        overdraft_limit = float(record['overdraft_limit'])
                        overdraft_rate = float(record['overdraft_rate'])
                        account = ChequingAccount(account_number,
                                                  client_number, balance, date_created,overdraft_limit, overdraft_rate)
                        
                    elif account_type == "InvestmentAccount":
                        management_fee = float(record['management_fee'])
                        account = InvestmentAccount(account_number,
                                                    client_number, balance, date_created, management_fee)
                    elif account_type == "SavingsAccount":
                        minimum_balance = float(record['minimum_balance'])
                        account = SavingsAccount(account_number, client_number, balance, date_created, minimum_balance)
                    else:
                        raise ValueError("Not a valid account type.")

                    accounts[account_number] = account
                except Exception as e:
                    logging.error(f"Unable to create bank account: {str(e)}")

    return client_listing, accounts


def update_data(updated_account: BankAccount) -> None:
    """
    Updates the accounts.csv file with balance data provided in the BankAccount argument.

    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []
    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            if account_number == updated_account.account_number:
                    row['balance'] = updated_account.balance
                
    # Write updated data
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients, accounts = load_data()

    if not clients or not accounts:
        print("No data loaded!")
    else:
        print("=========================================")
        for client in clients.values():
            print(client)
            print(f"{client.client_number} Accounts\n=============")
            for account in accounts.values():
                if account.client_number == client.client_number:
                    print(f"{account}\n")
            print("=========================================")

