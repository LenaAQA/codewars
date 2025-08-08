"""
Link: https://www.codewars.com/kata/5637b03c6be7e01d99000046
"""


def make_password(phrase):
    password = ""
    for i in phrase.split():
        i = i[0]
        if i in "iI":
            password += "1"
        elif i in "oO":
            password += "0"
        elif i in "sS":
            password += "5"
        else:
            password += i
    return password


print(make_password("Give me liberty or give me death"))
