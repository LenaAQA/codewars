"""
Link: https://www.codewars.com/kata/55d410c492e6ed767000004f
"""


def vowel_2_index(string):
    result = ""
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            result += str(i + 1)
        else:
            result += string[i]
    return result


print(vowel_2_index('this is my string'))
