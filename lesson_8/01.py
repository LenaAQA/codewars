"""
Link: https://www.codewars.com/kata/56a25ba95df27b7743000016
"""


def validate_code(code):
    return bool([symbol for symbol in "123" if symbol == str(code)[0]])


print(validate_code(123))
