from typing import Any

from src.masks import account_mask, card_mask


def card_or_account_mask(number: str) -> str:
    """Функция принимает строку с типом и номером карты или счёта, и возвращает эти данные в замаскированном виде"""

    account_numbers: Any = []
    card_numbers: Any = []

    if number[-5].isdigit():
        """Цикл, определяющий, с какими входными данными работает функция: номер карты или счёта"""

        account_numbers.append(number[-20:])
        account_numbers = "".join(account_numbers)
        masked_account = account_mask(account_numbers)
        result = f"{number[:4]} {masked_account}"

    elif number[-5] == " ":
        card_numbers.append(number[-19:])
        card_numbers = "".join(card_numbers)
        card_numbers = card_numbers.replace(" ", "")
        masked_card = card_mask(card_numbers)
        result = f"{number[:-19]} {masked_card}"

    return result


print(card_or_account_mask("Visa Platinum 7000 7922 8960 6361"))
