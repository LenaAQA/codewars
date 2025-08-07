"""
Link: https://www.codewars.com/kata/605d25f4f24c030033da9afb
"""


def convert_lambda_to_def(string):
    list_str = string.split()
    return f"def {list_str[0]}({list(str(list_str[3]).split(':'))[0]}):\n    return {string.split(':', 1)[1].strip()}"


print(convert_lambda_to_def("func = lambda a: a * 2"))
