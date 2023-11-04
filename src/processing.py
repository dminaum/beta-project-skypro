from widget import formatting_time


def filter_dicts_by_state(dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    :param dicts: Список словарей для фильтрации.
    :param state: Значение 'state', по которому производится фильтрация (по умолчанию 'EXECUTED').
    :return: Новый список, содержащий только словари с ключом 'state', равным заданному значению 'state'.
    """
    return [d for d in dicts if d.get("state") == state]


def filter_dicts_by_date(dicts: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по убыванию даты.
    :param dicts: Список словарей для сортировки.
    :param reverse: Определяет порядок сортировки (по умолчанию True для сортировки по убыванию).
    :return: Новый список, содержащий словари, отсортированные по убыванию даты
    (или по возрастанию, если reverse=False).
    """
    return sorted(dicts, key=lambda x: formatting_time(x["date"]), reverse=reverse)
