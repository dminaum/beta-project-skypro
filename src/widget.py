from masks import masking_account, masking_card


def masking_operation(account_number: str) -> str:
    """
    Функция принимает номер карты или счета и зашифровывает его
    :param account_number: Номер для маскирования
    :return: Маскированный по правилу номер карты или счета
    """
    number_splitted = account_number.split(" ")
    if len(number_splitted[-1]) == 20:
        return number_splitted[0] + " " + masking_account(number_splitted[-1])
    elif len(number_splitted[-1]) == 16:
        return " ".join(number_splitted[:-1]) + " " + masking_card(number_splitted[-1])
    else:
        return 'Неправильно введен номер карты/счета. Пожалуйста, попробуйте еще раз'


def formatting_time(time_: str) -> str:
    """
    Функция принимает время и возвращает в другом формате
    :param time_: входящая строка со временем и датой
    :return: Отформатированная по правилу дата
    """
    return time_[8:10] + "." + time_[5:7] + "." + time_[:4]
