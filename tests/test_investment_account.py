import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        self.investment_account = InvestmentAccount(67890, 201, 700.00, date(2024, 2, 15),1.50)

    def test_init_valid_values(self):
        investment_account = InvestmentAccount(67890, 201, 700.00, date(2024, 2, 15),1.50)

        self.assertEqual(investment_account._BankAccount__account_number, 67890)
        self.assertEqual(investment_account._BankAccount__client_number, 201)
        self.assertEqual(investment_account._BankAccount__balance, 700.00)
        self.assertEqual(investment_account._date_created, date(2024, 2, 15))
        self.assertEqual(investment_account._InvestmentAccount__management_fee, 1.50)

    def test_invalid_management_fee_with_invalid_value(self):
        investment_account = InvestmentAccount(67890, 201, 700.00, date(2024, 2, 15),"INVALID")
        self.assertEqual(investment_account._InvestmentAccount__management_fee, 2.55)

    def test_service_charge_old_investment_account(self):
        date_created = date.today() - timedelta( days=12 * 365)
        investment_account = InvestmentAccount(67890, 201, 700.00, date_created, 1.50)

        expected_service_charge = 0.50

        self.assertEqual(investment_account.get_service_charges(), expected_service_charge)

    def test_service_charge_10_year_old_investment_account(self):
        date_created = self.investment_account.TEN_YEARS_AGO
        investment_account = InvestmentAccount(67890, 201, 700.00, date_created, 1.50)

        expected_service_charge = 0.50
        self.assertEqual(investment_account.get_service_charges(), expected_service_charge)

    def test_service_charge_new_account(self):
        date_created = date.today() - timedelta(days=2 * 365)
        management_fee = 1.50
        investment_account = InvestmentAccount(67890, 201, 700.00, date_created, 1.50)

        expected_service_charge = 0.50 + management_fee

        self.assertEqual(investment_account.get_service_charges(), expected_service_charge)

    def test_string_representation_for_old_investment_account(self):
        date_created = date.today() - timedelta( days=12 * 365)
        investment_account = InvestmentAccount(67890, 201, 700.00, date_created, 1.50)
        expected_str = f"Account Number: {investment_account._BankAccount__account_number} Balance: ${investment_account._BankAccount__balance:,.2f}\nDate Created: {date_created} Management Fee: Waived Account Type: Investment"
        self.assertEqual(str(investment_account), expected_str)

    def test_string_representation_for_new_investment_account(self):
        date_created = date.today() - timedelta(days=2 * 365)
        investment_account = InvestmentAccount(67890, 201, 700.00, date_created, 1.50)
        expected_str = f"Account Number: {investment_account._BankAccount__account_number} Balance: ${investment_account._BankAccount__balance:,.2f}\nDate Created: {date_created} Management Fee: ${investment_account._InvestmentAccount__management_fee:,.2f}% Account Type: Investment"
        self.assertEqual(str(investment_account), expected_str)


if __name__ == '__main__':
    unittest.main()