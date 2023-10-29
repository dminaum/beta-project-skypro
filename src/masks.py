def masking_card(card_number: str) -> str:
    """
    Функция принимает номер карты и зашифровывает его
    :param card_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """

    if len(card_number) == 16:
        masked_card = card_number[:4] + card_number[4:6] + "** **** " + card_number[12:]
        return masked_card
    else:
        return "Неправильно введён номер карты"


def masking_account(account_number: str) -> str:
    """
    Функция принимает номер счета и зашифровывает его
    :param account_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """

    if len(account_number) == 20:
        masked_account = "**" + account_number[16:]
        return masked_account
    else:
        return "Неправильно введён номер счёта"
