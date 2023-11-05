import pytest
from src.widget import masking_operation, formatting_time

"""
Фикстура для подготовки данных тестов
"""


@pytest.fixture
def valid_card_numbers():
    return [
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654")
    ]


@pytest.fixture
def invalid_card_numbers():
    return [
        "Maestro 12345678901234567",
        "MasterCard 987654321098765"
    ]


@pytest.fixture
def valid_account_numbers():
    return [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 98765432109876543210", "Счет **3210")
    ]


@pytest.fixture
def invalid_account_numbers():
    return [
        "Счет 1234567890",
        "Счет 123456789012345678901"
    ]

"""
Тесты для функции operation
"""

