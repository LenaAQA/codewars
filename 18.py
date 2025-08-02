# Число перепутано с текстом. Ваша цель — восстановить число из текста


def filter_string(st):
    return int("".join([i for i in st if i.isdigit()]))


print(filter_string("aa1bb2cc3dd"))
