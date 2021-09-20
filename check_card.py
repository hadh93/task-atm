import re
import hyp_bank_api

def validate_card(card_info):
    card_info = card_info.split()
    if card_info[0] == "EXIT":
        print("GOOD BYE!")
        return False
    if len(card_info) != 2:
        print("ERROR: WRONG CARD INPUT")
        return False
    if card_info[1] not in hyp_bank_api.bank_db[0]:
        print("ERROR: UNREGISTERED CARD")
        return False
    return True


def is_valid_card(status):
    if status == "True":
        return True
    else:
        return False


def is_valid_number(num):
    regex = re.compile('[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}', re.I)
    match = regex.match(str(num))
    print(bool(match))
    return bool(match)
