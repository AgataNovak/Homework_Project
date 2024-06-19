import os
from typing import Union
from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_logs = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger('masks', file_path_logs)


def card_mask(card_number: Union[list, str, int]) -> str:
    """Функция принимает номер карты и возвращает его в замаскированном виде"""

    logger.info("Запуск функции card_mask")
    card_number = str(card_number)
    logger.info("Заданный номер карты замаскирован")
    masked_card_number = f"{card_number[0: 4]} {card_number[4: 6]}** **** {card_number[-4:]}"
    return masked_card_number


def account_mask(account_number: Union[list, str, int]) -> str:
    """Функция принимает номер счета и возвращает его в замаскированном виде"""

    logger.info("Запуск функции account_mask")
    account_number = str(account_number)
    logger.info("Данный номер счёта замаскирован")
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number
