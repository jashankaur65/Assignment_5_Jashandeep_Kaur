import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date 

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.savings_account = SavingsAccount(4532, 635, 2450.90, date(2025, 2, 8), 200)

    def test_init_valid_values(self):
        savings_account = SavingsAccount(4532, 635, 2450.90, date(2025, 2, 8), 200)

        self.assertEqual(savings_account._BankAccount__account_number, 4532)
        self.assertEqual(savings_account._BankAccount__client_number, 635)
        self.assertEqual(savings_account._BankAccount__balance, 2450.9)
        self.assertEqual(savings_account._date_created, date(2025, 2, 8))
        self.assertEqual(savings_account._SavingsAccount__minimum_balance, 200)

    def test_init_invalid_minimum_balance_type(self):
        savings_account = SavingsAccount(4532, 635, 2450.90, date(2025, 2, 8), "Invalid")
        self.assertEqual(savings_account._SavingsAccount__minimum_balance, 50)

    def test_balance_above_minimum_balance(self):
        savings_account = SavingsAccount(4532, 635, 3436.78, date(2025, 2, 8), 200)
        expected_service_charge = 0.50
        self.assertEqual(savings_account.get_service_charges(), expected_service_charge)
        
    def test_balance_equal_to_minimum(self):
        savings_account = SavingsAccount(4532, 635, 3436.78, date.today(), 200.0)
        expected_service_charge = 0.5  
        self.assertEqual(savings_account.get_service_charges(), expected_service_charge)


    def test_balance_below_minimum_balance(self):
        savings_account = SavingsAccount(4532, 635, 150.0, date(2025, 2, 8), 200)
        expected_service_charge = 0.50 * SavingsAccount.SERVICE_CHARGE_PREMIUM
        actual = round(savings_account.get_service_charges(), 2)
        self.assertEqual(actual, expected_service_charge)

    def test_str_representation(self):
        savings_account =SavingsAccount(4532, 635, 2450.90, date(2025, 2, 8), 200)
        expected_str = (f"Account Number: 4532 Balance: ${self.savings_account._BankAccount__balance:,.2f}"
                f"\nMinimum Balance: ${self.savings_account._SavingsAccount__minimum_balance:.2f} Account Type: Savings")
        self.assertEqual(str(savings_account), expected_str)
    