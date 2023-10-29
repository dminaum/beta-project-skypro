def masking_card2(card_number: str) -> str:
    """
    Функция принимает номер карты и зашифровывает его
    :param card_number: Номер для маскирования
    :return: Маскированный по правилу номер карты
    """
    for i, s in enumerate(card_number):
        if s.isdigit():
            break
    return card_number[:i + 4] + ' ' + card_number[i + 5:i + 7] + '** **** ' + card_number[i + 12:]


def masking_account2(account_number: str) -> str:
    """
    Функция принимает номер счета и зашифровывает его
    :param account_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    for i, s in enumerate(account_number):
        if s.isdigit():
            break
    return account_number[:5] + '**' + account_number[-4:]


def formatting_time(time_: str) -> str:
    """
    Функция принимает время и возвращает в другом формате
    :param time_: входящая строка со временем и датой
    :return: Отформатированная по правилу дата
    """
    return time_[8:10] + '.' + time_[5:7] + '.' + time_[:4]
