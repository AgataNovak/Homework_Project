import json
from src.external_api import currency_conversion
from dotenv import load_dotenv
import os
import logging


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def get_transactions_info(path_to_json):
    """Фунция принимает путь до файла и возвращает содержимое JSON файла"""

    logger.info("Запущена функция get_transaction_info")
    try:
        logger.info(f"Открытие файла с указанным путём: {path_to_json}")
        with open(path_to_json) as f:
            try:
                data = json.load(f)
                logger.info("Получение данных из JSON файла")
                return data
            except json.JSONDecodeError as ex:
                logger.error(f"Ошибка получения данных JSON формата: {ex}")
                return []
    except FileNotFoundError as ex:
        logger.error(f"Ошибка, файл не найден: {ex}")
        return []


def amount_of_transaction(transaction_json):
    """Функция принимает JSON строку с информацией о транзакции и возвращает сумму данной транзакции"""
    logger.info("Запуск функции amount_of_transaction")
    try:
        logger.info("Получение значения amount - суммы транзакции")
        currency = transaction_json[0]["operationAmount"]["currency"]["code"]
        amount = transaction_json[0]["operationAmount"]["amount"]
        if currency != "RUB":
            logger.info(f"Конвертация валюты {currency} в рубли")
            amount = currency_conversion(currency, amount, API_KEY)
        return amount
    except KeyError as ex:
        logger.info(f"Ошибка получения суммы транзакции: {ex}")
        return []
