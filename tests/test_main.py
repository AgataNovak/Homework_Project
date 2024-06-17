import pytest
from src.main import transactions
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.widget import card_or_account_mask, date_formating
from src.decorators import log


@pytest.mark.parametrize(
    "number_of_account_or_card, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 00000000000000000000", "Счет **0000"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum  7000 79** **** 6361"),
        ("Visa Platinum 1234 5678 9012 3456", "Visa Platinum  1234 56** **** 3456"),
        ("Visa Master Card 0000 0000 0000 0000", "Visa Master Card  0000 00** **** 0000"),
        ("GasPromBank 1234 1234 1234 1234", "GasPromBank  1234 12** **** 1234"),
    ],
)
def test_card_or_account_mask(number_of_account_or_card, expected):
    assert card_or_account_mask(number_of_account_or_card) == expected


def test_card_or_account_mask_empty_string(nothing):
    with pytest.raises(IndexError):
        assert card_or_account_mask("")


@pytest.mark.parametrize(
    "date_old_format, expected",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_date_formating(date_old_format, expected):
    assert date_formating(date_old_format) == expected


def test_date_formating_empty(nothing):
    with pytest.raises(IndexError):
        assert card_or_account_mask("")


def test_filter_by_currency_usd():
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941


def test_filter_by_currency_rub():
    rub_transactions = filter_by_currency(transactions, "руб.")
    assert next(rub_transactions)["id"] == 873106923
    assert next(rub_transactions)["id"] == 594226727


def test_transaction_descriptions():
    description = transaction_descriptions(transactions)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"


def test_card_number_generator():
    card_number_generated = card_number_generator(123456, 123460)
    assert next(card_number_generated) == "0000 0000 0012 3456"
    assert next(card_number_generated) == "0000 0000 0012 3457"
    assert next(card_number_generated) == "0000 0000 0012 3458"
    assert next(card_number_generated) == "0000 0000 0012 3459"


def test_log(capsys):
    @log()
    def addition(x, y):
        return x + y

    addition(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "Function addition ok. Returned 5\n"

    addition(2, "3")
    captured = capsys.readouterr()
    assert captured.out == "addition error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (2, '3'), {}\n"

    addition("7", [2, 3, 4])
    captured = capsys.readouterr()
    assert (
        captured.out
        == """addition error: can only concatenate str (not "list") to str. Inputs: ('7', [2, 3, 4]), {}\n"""
    )
