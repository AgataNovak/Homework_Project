import pytest
from src.widget import card_or_account_mask, date_formating


def test_account_mask(number_of_account):
    assert card_or_account_mask(number_of_account) == 'Счет **4305'


def test_card_mask(number_of_card):
    assert card_or_account_mask(number_of_card) == 'Visa Platinum  7000 79** **** 6361'


def test_card_or_account_mask_empty_string():
    with pytest.raises(IndexError):
        assert card_or_account_mask('')


def test_card_or_account_mask_no_arg():
    with pytest.raises(TypeError):
        assert card_or_account_mask()


def test_date_formating(date_old_format):
    assert date_formating(date_old_format) == '11.07.2018'
