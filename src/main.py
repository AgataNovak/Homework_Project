import os

from src.decorators import log
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import executed_dicts, sorted_dicts
from src.utils import (amount_of_transaction, get_transactions_info_csv, get_transactions_info_excel,
                       get_transactions_info_json)
from src.widget import card_or_account_mask, date_formating

print(card_or_account_mask("Счет 73654108430135874305"))
print(card_or_account_mask("Visa Platinum 7000 7922 8960 6361"))
print(date_formating("2018-07-11T02:26:18.671407"))

dicts = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(executed_dicts(dicts, "CANCELED"))
print(sorted_dicts(dicts, False))


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


usd_transactions = filter_by_currency(transactions, "USD")
for i in range(3):
    print(next(usd_transactions)["id"])


description = transaction_descriptions(transactions)
for a in range(5):
    print(next(description))


for card_number in card_number_generator(1234567, 1234569):
    print(card_number)


@log()
def addition(x, y):
    return x + y


print(addition(5, 3))
addition(5, "3")


path_to_json = os.path.abspath("../data/operations.json")
path_to_csv = os.path.abspath("../data/transactions.csv")
path_to_excel = os.path.abspath("../data/transactions_excel.xlsx")

print(get_transactions_info_json(path_to_json))

print(type(get_transactions_info_csv(path_to_csv)))
print(get_transactions_info_csv(path_to_csv))

print(get_transactions_info_excel(path_to_excel))


transaction_rub = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }
]
print(amount_of_transaction(transaction_rub))

transaction_usd = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "100", "currency": {"name": "dollar", "code": "USD"}},
    }
]

print(amount_of_transaction(transaction_usd))

print(get_transactions_info_csv(path_to_csv))
print(get_transactions_info_excel(path_to_excel))
