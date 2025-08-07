"""
Аккуратное число — это число, цифры которого расположены в неубывающем порядке.
Задача
По заданному числу определите, аккуратно оно или нет.
Примечания
Переданное число всегда будет положительным.
Верните результат как логическое значение.
Link: https://www.codewars.com/kata/5a87449ab1710171300000fd
"""


def tidyNumber(n):
    s = str(n)
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            return False
    return True


print(tidyNumber(12))
print(tidyNumber(102))
