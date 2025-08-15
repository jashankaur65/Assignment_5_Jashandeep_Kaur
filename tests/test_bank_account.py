"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "Arshdeep Kaur"
__version__ = "1.0.0"

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(12345, 6789, 100.0)

    def test_init_input_values_attributes_set(self):
        # Arrange & Act
        bank_account = BankAccount(12345, 6789, 100.0)
        #  Assert
        self.assertEqual(bank_account.account_number, 12345)
        self.assertEqual(bank_account.client_number, 6789)
        self.assertEqual(bank_account.balance, 100.0)

    def test_init_non_numeric_balance_set_to_zero(self):
        account = BankAccount(12345, 6789, 'not_a_number')
        self.assertEqual(account.balance, 0.0)

    def test_init_invalid_account_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            BankAccount('invalid', 6789, 100.0)

    def test_init_invalid_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            BankAccount(12345, 'invalid', 100.0)

    def test_account_number_getter_returns_account_number(self):
        self.assertEqual(self.account.account_number, 12345)

    def test_client_number_getter_returns_client_number(self):
        self.assertEqual(self.account.client_number, 6789)

    def test_balance_getter_returns_balance(self):
        self.assertEqual(self.account.balance, 100.0)

    def test_update_balance_when_positive_amount_recieved(self):
        self.account._update_balance(50.0)
        self.assertEqual(self.account.balance, 150.0)

    def test_update_balance_when_negative_amount_recieved(self):
        self.account._update_balance(-50.0)
        self.assertEqual(self.account.balance, 50.0)
    
    def test_unchanged_balance_when_non_numeric_amount_received(self):
        initial_balance = self.account.balance
        with self.assertRaises(ValueError):
            self.account._update_balance('invalid')
        self.assertEqual(self.account.balance, initial_balance)
    
    def test_balance_updated_correctly_when_valid_amount_deposited(self):
        self.account.deposit(20.0)
        self.assertEqual(self.account.balance, 120.0)

    def test_deposit_raises_valueerror_when_negative_amount_provided(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-20.0)

    def test_balance_updated_correctly_when_valid_amount_provided(self):
        self.account.withdraw(30.0)
        self.assertEqual(self.account.balance, 70.0)

    def test_withdraw_negative_amount_raises_valueerror(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-30.0)

    def test_withdraw_raises_valueerror_when_amount_exceeds_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(160.0)

    def test_str_returns_str_in_expected_format(self):
        expected_str = "Account Number: 12345 Balance: $100.00"
        self.assertEqual(str(self.account), expected_str)



        
        

