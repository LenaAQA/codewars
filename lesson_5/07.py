"""
Возвращает количество гласных в заданной строке.
Мы будем считать a, e, i, o, u гласными для этого Ката (но не y).
Входная строка будет состоять только из строчных букв и/или пробелов.
Link: https://www.codewars.com/kata/54ff3102c1bad923760001f3
"""


def get_count(sentence):
    res = 0
    for i in sentence:
        if i in "aeiou":
            res += 1
    return res


print(get_count("aeiou"))
