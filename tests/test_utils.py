import os.path
import unittest
from unittest.mock import patch

from src.external_api import currency_conversion
from dotenv import load_dotenv
from src.utils import get_transactions_info, amount_of_transaction

load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open")
    def test_get_transactions_info(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = \
            ('[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount":'
             ' {"amount": "31957.58", "currency": {"name": "\u0440\u0443\u0431.", "code": "RUB"}}}]')

        transactions = get_transactions_info("test_file.json")
        self.assertEqual(
            transactions,
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {
                        "amount": "31957.58",
                        "currency": {"name": "\u0440\u0443\u0431.", "code": "RUB"},
                    },
                }
            ],
        )

    @patch("builtins.open")
    def test_get_transactions_info_empty(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = "[]"
        transactions = get_transactions_info("test_file.json")
        self.assertEqual(transactions, [])

    def test_get_transactions_info_not_found(self):
        transactions = get_transactions_info("file_does_not_exist")
        self.assertEqual(transactions, [])


class TestSumOfTransactions(unittest.TestCase):

    def test_amount_of_transaction_rub(self):
        transaction = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "\u0440\u0443\u0431.", "code": "RUB"}},
            }
        ]
        result = amount_of_transaction(transaction)
        self.assertEqual(result, "31957.58")


class TestExternalApi(unittest.TestCase):

    @patch("requests.request")
    def test_currency_conversion_usd(self, mock_get):
        mock_get.return_value.json.return_value = {"result": 7500.0}
        mock_get.return_value.status_code = 200
        currency = "USD"
        amount = 100
        result = currency_conversion(currency, amount)
        self.assertEqual(result, 7500.0)
        mock_get.assert_called_once_with(
            "GET",
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
            headers=headers,
        )
