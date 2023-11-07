import pytest
from src.widget import masking_operation, formatting_time


@pytest.mark.parametrize('input_number, expected_result', [
    ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Счет 98765432109876543210", "Счет **3210")
])
def test_masking_operation_valid(input_number, expected_result):
    assert masking_operation(input_number) == expected_result


@pytest.mark.parametrize('invalid_number', [
    "Maestro 12345678901234567",
    "MasterCard 987654321098765",
    "Счет 1234567890",
    "Счет 123456789012345678901"
])
def test_masking_operation_invalid(invalid_number):
    assert masking_operation(invalid_number) == 'Неправильно введен номер карты/счета. Пожалуйста, попробуйте еще раз'


@pytest.mark.parametrize('time_, expected_result', [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2001-01-06T02:26:18.671407", "06.01.2001"),
    ("2000-11-30T02:26:18.671407", "30.11.2000"),
])
def test_formatting_time(time_, expected_result):
    assert formatting_time(time_) == expected_result
