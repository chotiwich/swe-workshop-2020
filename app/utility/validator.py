def validate_name(name):
    blacklist = ["0", "1", "2", "3", "4", "5",
                 "6", "7", "8", "9", "!", "@", "#", "$", ' ', ""]

    if name == "":
        return False

    for charactor in name:

        if charactor in blacklist:
            return False

    return True


def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
