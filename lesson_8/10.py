"""
Link: https://www.codewars.com/kata/55ee3ebff71e82a30000006a
"""


def title_to_number(title):
    result = 0
    for char in title:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result


print(title_to_number('BA'))
