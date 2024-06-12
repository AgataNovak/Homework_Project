import json
from src.external_api import currency_conversion
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def get_transactions_info(path_to_json):
    """Фунция принимает путь до файла и возвращает содержимое JSON файла"""
    try:
        with open(path_to_json) as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def amount_of_transaction(transaction_json):
    """Функция принимает JSON строку с информацией о транзакции и возвращает сумму данной транзакции"""
    try:
        currency = transaction_json[0]["operationAmount"]["currency"]["code"]
        amount = transaction_json[0]["operationAmount"]["amount"]
        if currency != "RUB":
            amount = currency_conversion(currency, amount, API_KEY)
        return amount
    except KeyError:
        return []
