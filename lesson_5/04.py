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
    word1 = arr[0]
    word2 = arr[1]
    max_len = max(len(word1), len(word2))
    return '\n'.join(
        f"{word1[i] if i < len(word1) else ' '} {word2[i] if i < len(word2) else ' '}" for i in range(max_len))


print(transpose_two_strings(["Hello", "World"]))
