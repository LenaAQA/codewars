"""
Возвращает количество гласных в заданной строке.
Мы будем считать a, e, i, o, u гласными для этого Ката (но не y).
Входная строка будет состоять только из строчных букв и/или пробелов.
Link: https://www.codewars.com/kata/54ff3102c1bad923760001f3
"""


def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter in "aeiou":
            count += 1
    return count


print(get_count("aeiou"))
