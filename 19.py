# Ваша задача — просто подсчитать общее количество строчных букв в строке.


def lowercase_count(strng):
    return len([i for i in strng if i.islower()])


print(lowercase_count("abcABC123"))
