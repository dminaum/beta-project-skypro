def masking_card2(card_number: str) -> str:
    for i, s in enumerate(card_number):
        if s.isdigit():
            break
    return card_number[:i+4] + ' ' + card_number[i+5:i+7]  + '** **** ' + card_number[i+12:]
