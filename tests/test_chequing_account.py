import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.chequing_account = ChequingAccount(67890, 201, 700.00, date(2024, 2, 15), 200.0, 0.10)

    def test_init_valid_values_attributes_set(self):
        chequing_account = ChequingAccount(67890, 201, 700.00, date(2024, 2, 15), 200.0, 0.10)

        self.assertEqual(chequing_account._BankAccount__account_number, 67890)
        self.assertEqual(chequing_account._BankAccount__client_number, 201)
        self.assertEqual(chequing_account._BankAccount__balance, 700.00)
        self.assertEqual(chequing_account._date_created, date(2024, 2, 15))
        self.assertEqual(chequing_account._ChequingAccount__overdraft_limit, 200.0)
        self.assertEqual(chequing_account._ChequingAccount__overdraft_rate, 0.10)

    def test_invalid_overdraft_limit_type_set_to_default_value(self):
        chequing_account = ChequingAccount(67890, 201, 700.00, date(2024, 2, 15),"INVALID", 0.10)
        self.assertEqual(-100.00, chequing_account._ChequingAccount__overdraft_limit)

    def test_invalid_overdraft_rate_type_set_to_default_value(self):
        chequing_account = ChequingAccount(67890, 201, 700.00, date(2024, 2, 15), 200, "INVALID")
        self.assertEqual(0.5,chequing_account._ChequingAccount__overdraft_rate)
    
    def test_invalid_date_type_set_to_current_date(self):
        chequing_account = ChequingAccount(67890, 201, 700.00, "INVALID date", 200, 0.10)
        self.assertEqual(chequing_account._date_created, date.today())

    def test_service_charge_when_balance_is_above_overdraft_limit(self):
        chequing_account = ChequingAccount(67890, 201, 7000.00, date(2024, 2, 15), 200, 0.10)
        expected_service_charge = 0.50
        self.assertEqual(chequing_account.get_service_charges(), expected_service_charge)

    def test_service_charge_when_balance_is_below_overdraft_limit(self):
        chequing_account = ChequingAccount(67890, 201,700.0,2024-2-15, 2000, 0.10)
        expected_service_charge = 0.50
        actual = round(chequing_account.get_service_charges(), 2)
        self.assertEqual(actual, expected_service_charge)

    def test_service_charge_balance_equal_to_overdraft_limit(self):
        chequing_account = ChequingAccount(67890, 201, 200, 2024-2-15, 200, 0.10)
        expected_service_charge = 0.50
        self.assertEqual(chequing_account.get_service_charges(), expected_service_charge)
    
    def test_str_representation(self):
        chequing_account = ChequingAccount(67890, 201, 700.00,2024-2-15, 200.0, 0.10)
        expected_str =(f"Account Number: 67890 Balance: $700.00\n"
                f"Overdraft Limit: $200.00 Overdraft Rate: 10.00% Account Type: Chequing")
        self.assertEqual(str(chequing_account), expected_str)


if __name__ == '__main__':
    unittest.main()