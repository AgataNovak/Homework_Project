from src.processing import executed_dicts
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
