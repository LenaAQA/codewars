"""
Link: https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023
"""


def validate_usr(username):
    result = []
    if 4 <= len(username) <= 16:
        for i in username:
            if i.islower() or i.isdigit() or i == "_":
                result.append(True)
    return 0 < len(username) == len(result)


print(validate_usr(''))
