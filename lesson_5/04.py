"""
Вам будет предоставлен массив, содержащий две строки.
Ваша задача — создать функцию, которая возьмёт эти две строки и переставит их так,
чтобы они шли сверху вниз, а не слева направо.
e.g. transposeTwoStrings(['Hello','World']);
should return
H W
e o
l r
l l
o d
Несколько вещей, на которые следует обратить внимание:
Между двумя символами должен быть один пробел.
Вам не нужно менять регистр (т.е. не нужно менять на верхний или нижний)
Если одна строка длиннее другой, должен быть пробел на месте символа.
Link: https://www.codewars.com/kata/581f4ac139dc423f04000b99
"""


def transpose_two_strings(arr):
    s_1 = arr[0]
    s_2 = arr[1]
    max_len = max(len(s_1), len(s_2))
    return '\n'.join(f"{s_1[i] if i < len(s_1) else ' '} {s_2[i] if i < len(s_2) else ' '}" for i in range(max_len))


print(transpose_two_strings(["Hello", "World"]))

