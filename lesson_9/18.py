"""
Link: https://www.codewars.com/kata/56a24b4d9f3671584d000039
"""


def double_check(string):
    string = string.lower()
    for i in range(len(string) - 2):
        sim = string[i]
        if sim == string[i + 1]:
            return True
    return False


print(double_check("aabc"))
