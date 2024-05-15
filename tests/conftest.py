import pytest


@pytest.fixture
def number_of_account():
    return "Счет 73654108430135874305"


@pytest.fixture
def number_of_card():
    return "Visa Platinum 7000 7922 8960 6361"


@pytest.fixture
def date_old_format():
    return "2018-07-11T02:26:18.671407"
