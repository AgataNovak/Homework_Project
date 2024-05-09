from typing import Union


def card_mask(card_number: Union[str, int]) -> str:
    """ Функция принимает номер карты и возвращает его в замаскированном виде """
    card_number = str(card_number)
    masked_card_number = f"{card_number[0: 4]} {card_number[4: 6]}** **** {card_number[-4:]}"
    return masked_card_number


def account_mask(account_number: Union[str, int]) -> str:
    """ Функция принимает номер счета и возвращает его в замаскированном виде """
    account_number = str(account_number)
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number

