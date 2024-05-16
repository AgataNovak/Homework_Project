import pytest

from src.widget import card_or_account_mask, date_formating


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
