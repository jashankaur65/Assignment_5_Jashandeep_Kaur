"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Arshdeep Kaur"
__version__ = "1.0.0"

import unittest
from email_validator import EmailNotValidError
from client.client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(8,"Arshdeep", "Kaur",
                              "arshdeepdhiman969@gmail.com")


    def test_init_input_values_attributes_set(self):
        # Arrange & Act
        client = Client(8, "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
        
        #  Assert
        self.assertEqual(client.client_number, 8)
        self.assertEqual(client.first_name, "Arshdeep")
        self.assertEqual(client.last_name, "Kaur")
        self.assertEqual(client.email_address, "arshdeepdhiman969@gmail.com")
        

    def test_invalid_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client("INVALID", "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
    
    def test_blank_first_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client(8,"", "Kaur", "arshdeepdhiman969@gmail.com")

    def test_blank_last_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client(8,"Arshdeep", "", "arshdeepdhiman969@gmail.com")
    
    def test_invalid_email_address_raises_EmailNotValidError(self):
        with self.assertRaises(EmailNotValidError):
            Client(8, "Arshdeep", "Kaur", "")

    def test_client_number_accessor_valid_client_number_returned(self):
        client = Client(8, "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
        self.assertEqual(client.client_number, 8)
    
    def test_first_name_accessor_valid_first_name_returned(self):
        client = Client(8, "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
        self.assertEqual(client.first_name, "Arshdeep")

    def test_last_name_accessor_valid_last_name_returned(self):
        client = Client(8, "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
        self.assertEqual(client.last_name, "Kaur")
    
    def test_email_address_accessor_valid_email_address_returned(self):
        client = Client(8, "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
        self.assertEqual(client.email_address, "arshdeepdhiman969@gmail.com")

    def test_str_in_expected_format_returned(self):
        client = Client(8, "Arshdeep", "Kaur", "arshdeepdhiman969@gmail.com")
        expected_str = "Kaur, Arshdeep,[8] - arshdeepdhiman969@gmail.com"
        self.assertEqual(str(client), expected_str)
        










