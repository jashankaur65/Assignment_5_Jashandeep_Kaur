__author__ = "Jashandeep Kaur"
__version__ = "1.0.0"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from PySide6.QtCore import Slot
import copy
from ui_superclasses.details_window import DetailsWindow

class ClientLookupWindow(LookupWindow):
    """
    A window for looking up client information and bank information.
    
    Args:
        client_listing (dict): A dictionary mapping client numbers
        to Client objects.
        accounts (dict): A dictionary mapping account numbers
        to BankAccount objects. 
    """
    def __init__(self):
        """
        Initializes the ClientLookupWindow.
        """
        super().__init__()
        client_data, account_data = load_data()
        self.client_listing = client_data
        self.accounts = account_data
        
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)
    
    @Slot()
    def on_lookup_client(self):
        """
        Handles the lookup button click event to search for a client.
        """
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.warning(
                self,
                "Input Error",
                "The client number must be a numeric value."
            )
            self.reset_display()
            return
        
        if client_number not in self.client_listing:
            QMessageBox.information(
                self,
                "Client Not Found",
                f"Client number: {client_number} not found"
            )
            self.reset_display()
            return
            
        client = self.client_listing[client_number]
        full_name = f"{client.first_name} {client.last_name}"
        self.client_info_label.setText(f"Client Name: {full_name}")
        
        self.account_table.setRowCount(0)
        row = 0
        for account in self.accounts.values():
            if account.client_number == client_number:
                self.account_table.insertRow(row)

                try:
                    account_number_item = QTableWidgetItem(str(account.account_number))
                    balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                    date_created_item = QTableWidgetItem(str(account.date_created))
                    account_type_item = QTableWidgetItem(account.__class__.__name__)

                    account_number_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    date_created_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    account_type_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                    self.account_table.setItem(row, 0, account_number_item)
                    self.account_table.setItem(row, 1, balance_item)
                    self.account_table.setItem(row, 2, date_created_item)
                    self.account_table.setItem(row, 3, account_type_item)

                    row += 1
                    self.__toggle_filter(False)

                except AttributeError as e:
                    QMessageBox.warning(
                        self,
                        "Data Error",
                        f"Invalid account data: {e}"
                    )
                    continue

        self.account_table.resizeColumnsToContents()
        
    @Slot()
    def on_text_changed(self):
        """
        Clears the account_table whenever the text in
        client_number_edit changes.
        """
        self.account_table.setRowCount(0)
        
    @Slot(int, int)
    def on_select_account(self, row: int, column: int) ->None:
        """
        Handles a click on a cell in account_table
         to open an AccountDetailsWindow for the selected account.
        
        Args:
            row (int): The row number of the clicked cell
            column (int): The column number of the clicked cell
        """
        account_number_item = self.account_table.item(row, 0)
        if not account_number_item or not account_number_item.text().strip():
            QMessageBox.information(
                self,
                "Invalid Selection",
                "Please select a valid record."
            )
            return
        try:
            account_number = int(account_number_item.text().strip())
        except ValueError:
            QMessageBox.information(
                self,
                "Invalid Account Number",
                "Account number must be a valid integer."
            )
            return
        if account_number not in self.accounts:
            QMessageBox.information(
                self,
                "No Bank Account",
                "Bank Account does not exist."
            )
            return
        bank_account = self.accounts[account_number]
        account_details_window = AccountDetailsWindow(bank_account)
        account_details_window.exec_()
        account_details_window.balance_updated.connect(self.update_data)
        account_details_window.exec_()
        
    @Slot(BankAccount)
    def update_data(self, account: BankAccount) -> None:
        """
        Slot method to handle the balance_updated signal
        from AccountDetailsWindow.
        Updates the account_table, accounts dictionary,
        and saves the data.

        Args:
            account (BankAccount): The updated BankAccount object.
        """
        for row in range(self.account_table.rowCount()):
            table_account_number_item = self.account_table.item(row, 0)
            if table_account_number_item:
                table_account_number = int(table_account_number_item.text())
                if table_account_number == account.account_number:
                    balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                    balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    self.account_table.setItem(row, 1, balance_item)
                    break


        self.accounts[account.account_number] = account
        update_data(self.client_listing, self.accounts)
        
    @Slot()
    def __on_filter_clicked(self):
        """
        This function runs when you click the filter button.
        If the button says "Reset," it clears the filter
        and shows all the rows again.
        It also updates how the interface looks by calling
        the __toggle_filter() method.
        """
        if self.filter_button.text() == "Apply Filter":
            row_count = self.account_table.rowCount()
            column_index = self.filter_combo_box.currentIndex()
            search_text = self.filter_edit.text().lower()

            matching_rows = [
                i for i in range(row_count)
                if self.account_table.item(i, column_index) is not None
                and search_text in self.account_table.item(i, column_index).text().lower()
            ]

            for i in range(row_count):
                self.account_table.setRowHidden(i, i not in matching_rows)
            self.__toggle_filter(True)
        else:
            for i in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(i, False)
            self.__toggle_filter(False)

    @Slot()
    def __toggle_filter(self, filter_on: bool):
        """
        Toggles the filter mode for the UI elements.

        Args:
        filter_on (bool): Whether the filter is currently 
        applied or not.
        """
        self.filter_button.setEnabled(True)
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered")
