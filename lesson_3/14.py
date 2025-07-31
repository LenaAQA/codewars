# Получив букву, укажите ее положение в алфавите.
#
# Ввод :: "а"
#
# Вывод :: "Позиция алфавита: 1"
#
# Примечание: проверяются только строчные буквы английского языка.


def position(letter):
    import string
    al = string.ascii_lowercase
    return f"Position of alphabet: {al.index(letter) + 1}"


print(position("a"))
