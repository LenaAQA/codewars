"""
Получив букву, укажите ее положение в алфавите.
Ввод: "а"
Вывод: "Позиция алфавита: 1"
Примечание: проверяются только строчные буквы английского языка.
Link: https://www.codewars.com/kata/5808e2006b65bff35500008f
"""


def position(letter):
    import string
    al = string.ascii_lowercase
    return f"Position of alphabet: {al.index(letter) + 1}"


print(position("a"))
