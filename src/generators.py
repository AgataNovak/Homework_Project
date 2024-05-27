def filter_by_currency(list_of_transactions, currency):
    """Функция принимает список данных о транзакциях и валюту, и возвращает список транзакций с указанной валютой"""

    transactions_by_currency = list(
        transaction
        for transaction in list_of_transactions
        if transaction["operationAmount"]["currency"]["name"] == currency
    )
    for transaction in transactions_by_currency:
        yield transaction


# usage example
# usd_transactions = filter_by_currency(transactions, 'USD')
# for i in range(3):
#     print(next(usd_transactions)['id'])


def transaction_descriptions(list_of_transactions):
    """Функция которая принимает список данных о транзакцяих, и возвращает описания транзакций"""

    for transaction in list_of_transactions:
        desc = transaction["description"]
        yield desc


# usage example
# description = transaction_descriptions(transactions)
# for a in range(5):
#     print(next(description))


def card_number_generator(start, stop):
    """Функция которая принимает диапазон номеров карт и возвращает сгенерированные номера карт"""

    for i in range(start, stop):
        length_of_zeroes = 16 - len(str(i))
        card_number_generated = f"{'0' * length_of_zeroes}{str(i)}"
        generated_number = (
            f"{card_number_generated[0: 4]} {card_number_generated[4: 8]} "
            f"{card_number_generated[8:12]} {card_number_generated[-4:]}"
        )
        yield generated_number


# usage example
# for card_number in card_number_generator(1234567, 1234569):
#     print(card_number)
