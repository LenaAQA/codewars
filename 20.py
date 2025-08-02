# Напишите простое регулярное выражение для проверки имени пользователя.
# Допустимые символы:
#
# строчные буквы,
# числа,
# подчеркивание
# Длина должна быть от 4 до 16 символов (включая оба).


def validate_usr(username):
    res = []
    if 4 <= len(username) <= 16:
        for i in username:
            if i.islower() or i.isdigit() or i == "_":
                res.append(True)
    return 0 < len(username) == len(res)


print(validate_usr(''))
