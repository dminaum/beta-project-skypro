def masking_card2(card_number: str) -> str:
    for i, s in enumerate(card_number):
        if s.isdigit():
            break
    return card_number[:i + 4] + ' ' + card_number[i + 5:i + 7] + '** **** ' + card_number[i + 12:]


def masking_account2(account_number: str) -> str:
    for i, s in enumerate(account_number):
        if s.isdigit():
            break
    return account_number[:5] + '**' + account_number[-4:]


def formatting_time(time_):
    return time_[8:10] + '.' + time_[5:7] + '.' + time_[:4]
