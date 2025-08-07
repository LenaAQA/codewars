"""
Link: https://www.codewars.com/kata/55e9529cbdc3b29d8c000016
"""


def char_to_ascii(s):
    letters = [chr(i) for i in range(65, 123)]
    if s != "":
        result = {}
        for i in s:
            if i.isalpha():
                result[i] = letters.index(i) + 65
        return result


print(char_to_ascii("a"))
