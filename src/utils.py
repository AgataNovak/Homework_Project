import csv
import json
import os

import pandas as pd
from dotenv import load_dotenv

from src.external_api import currency_conversion

from src.logger import setup_logger

load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_logs = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_logs)


def get_transactions_info_json(path_to_json):
    """Фунция принимает путь до файла и возвращает содержимое JSON файла"""

    logger.info("Запущена функция get_transaction_info")
    try:
        logger.info(f"Открытие JSON файла с указанным путём: {path_to_json}")
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


def get_transactions_info_csv(path_to_csv):
    """Функция принимает путь до файла и возврашает содержимое CSV файла"""

    logger.info("Запуск функции get_transactions_info_csv")
    try:
        with open(path_to_csv, "r", encoding="utf-8") as f:
            logger.info(f"Открытие файла {f}")
            data = csv.DictReader(f, delimiter=";")
            list_of_rows = []
            for row in data:
                list_of_rows.append(row)
            logger.info(f"Получение данных из файла {f}")
            return list_of_rows
    except FileNotFoundError as ex:
        logger.error(f"Ошибка, файл не найден: {ex}")
        return []


def get_transactions_info_excel(path_to_excel):
    """Функция принимает путь до файла и возврашает содержимое EXCEL файла"""

    logger.info("Запуск функции get_transactions_info_excel")
    try:
        with open(path_to_excel, "rb") as f:
            logger.info(f"Открытие файла {f}")
            data = pd.read_excel(f)
            logger.info(f"Получение данных из файла {f}")
            return data.to_dict("records")
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
