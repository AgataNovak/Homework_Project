import os.path
import unittest
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd
from dotenv import load_dotenv

from src.external_api import currency_conversion
from src.utils import (amount_of_transaction, get_transactions_info_csv, get_transactions_info_excel,
                       get_transactions_info_json)

load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


class TestGetTransactionsJSON(unittest.TestCase):

    @patch("builtins.open")
    def test_get_transactions_info_json(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = (
            '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount":'
            ' {"amount": "31957.58", "currency": {"name": "\u0440\u0443\u0431.", "code": "RUB"}}}]'
        )

        transactions = get_transactions_info_json("test_file.json")
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
    def test_get_transactions_info_json_empty(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = "[]"
        transactions = get_transactions_info_json("test_file.json")
        self.assertEqual(transactions, [])

    def test_get_transactions_info_not_found(self):
        transactions = get_transactions_info_json("file_does_not_exist")
        self.assertEqual(transactions, [])


class TestGetTransactionsCSV(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "4699552;EXECUTED;2022-03-23T08:29:37Z;23423;Peso;PHP;Discover 7269000803370165;"
        "American Express 1963030970727681;Перевод с карты на карту\n",
    )
    def test_get_transactions_info_csv(self, mock_file: MagicMock) -> None:
        result = get_transactions_info_csv("test.csv")
        self.assertEqual(
            result,
            [
                {
                    "id": "4699552",
                    "state": "EXECUTED",
                    "date": "2022-03-23T08:29:37Z",
                    "amount": "23423",
                    "currency_name": "Peso",
                    "currency_code": "PHP",
                    "description": "Перевод с карты на карту",
                    "from": "Discover 7269000803370165",
                    "to": "American Express 1963030970727681",
                }
            ],
        )

    @patch("pandas.read_csv")
    def test_get_transactions_info_csv_empty(self, mock_DictReader):
        mock_DictReader.return_value.__enter__.return_value.read.return_value = "[]"
        transactions = get_transactions_info_csv("test_path_to_csv_empty.csv")
        self.assertEqual(transactions, [])

    def test_get_transactions_info_csv_not_found(self):
        transactions = get_transactions_info_csv("file_does_not_exist.csv")
        self.assertEqual(transactions, [])


class GetTransactionsInfoExcel(unittest.TestCase):
    data = {
        "id": [4699552.0],
        "state": ["EXECUTED"],
        "date": ["2022-03-23T08:29:37Z"],
        "amount": [23423.0],
        "currency_name": ["Peso"],
        "currency_code": ["PHP"],
        "from": ["Discover 7269000803370165"],
        "to": ["American Express 1963030970727681"],
        "description": ["Перевод с карты на карту"],
    }

    df = pd.DataFrame(data)

    df.to_excel("test.xlsx", index=False)

    @patch("pandas.read_excel", return_value=df)
    def test_get_transactions_info_xlsx(self, mock_read_excel: MagicMock) -> None:
        result = get_transactions_info_excel("test.xlsx")
        self.assertEqual(
            result,
            [
                {
                    "id": 4699552.0,
                    "state": "EXECUTED",
                    "date": "2022-03-23T08:29:37Z",
                    "amount": 23423.0,
                    "currency_name": "Peso",
                    "currency_code": "PHP",
                    "description": "Перевод с карты на карту",
                    "from": "Discover 7269000803370165",
                    "to": "American Express 1963030970727681",
                }
            ],
        )

    @patch("pandas.read_excel")
    def test_get_transactions_info_excel_empty(self, mock_read_excel):
        mock_read_excel.return_value.__enter__.return_value.read.return_value = "[]"
        transactions = get_transactions_info_csv("test_path_to_excel_empty")
        self.assertEqual(transactions, [])

    def test_get_transactions_info_excel_not_found(self):
        transactions = get_transactions_info_excel("file_does_not_exist")
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
        result = currency_conversion(currency, amount, API_KEY)
        self.assertEqual(result, 7500.0)
        mock_get.assert_called_once_with(
            "GET",
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
            headers=headers,
        )
