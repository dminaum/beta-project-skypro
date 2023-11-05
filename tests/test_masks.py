import pytest
from src.masks import masking_card, masking_account

"""
Фикстура для подготовки данных тестов
"""


@pytest.fixture
def valid_card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654")
    ]


@pytest.fixture
def invalid_card_numbers():
    return [
        "123456789012345",
        "12345678901234567"
    ]


@pytest.fixture
def valid_account_numbers():
    return [
        ("12345678901234567890", "**7890"),
        ("98765432109876543210", "**3210")
    ]


@pytest.fixture
def invalid_account_numbers():
    return [
        "1234567890",
        "123456789012345678901"
    ]


"""
Тесты для функции masking_card
"""


@pytest.mark.parametrize("card_number, expected_masked_card", valid_card_numbers())
def test_masking_card_valid(card_number, expected_masked_card):
    assert masking_card(card_number) == expected_masked_card


@pytest.mark.parametrize("card_number", invalid_card_numbers())
def test_masking_card_invalid(card_number):
    assert masking_card(card_number) == "Неправильно введён номер карты"


"""
Тесты для функции masking_account
"""


@pytest.mark.parametrize("account_number, expected_masked_account", valid_account_numbers())
def test_masking_account_valid(account_number, expected_masked_account):
    assert masking_account(account_number) == expected_masked_account


@pytest.mark.parametrize("account_number", invalid_account_numbers())
def test_masking_account_invalid(account_number):
    assert masking_account(account_number) == "Неправильно введён номер счёта"
