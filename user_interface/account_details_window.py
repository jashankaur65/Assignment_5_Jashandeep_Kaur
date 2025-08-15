__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
from PySide6.QtCore import Signal, Slot
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform
    bank account transactions.
    
    Signals: 
        balance_updated: Emitted when the
        account balance is updated, passing
        the updated BankAccount.
    """
    balance_updated = Signal(BankAccount)
    
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        """
        super().__init__()
        if isinstance(account, BankAccount):
            self.account = copy.copy(account)
            self.account_number_label.setText(f"Account Number: {self.account.account_number}")
            self.balance_label.setText(f"Balance: {self.account.balance:.2f}")
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()
            
    def __on_apply_transaction(self):
        """
        Method for handling deposit or withdrawal transactions.
        """
    
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.information(
                self,
                "Invalid Data",
                "Amount must be numeric."
            )
            self.transaction_amount_edit.setFocus()
            return

        try:
            sender = self.sender()
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)
            else:
                return  


            self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")
            self.balance_updated.emit(self.account)
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            QMessageBox.information(
                self,
                f"{transaction_type} Failed",
                str(e)
            )
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    @Slot()
    def __on_exit(self):
        """
        Placeholder method for handling the exit button click.
        """
        self.close()