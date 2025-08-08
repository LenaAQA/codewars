"""
Link: https://www.codewars.com/kata/563a8656d52a79f06c00001f
"""


def is_valid(idn):
    result = []
    if len(idn) != 0 and (idn[0] in "_$" or idn[0].isalpha()):
        result.append(True)
        for i in idn[1:]:
            if i.isdigit() or i.isalpha() or i in "_$":
                result.append(True)
            else:
                return False
    return len(result) == len(idn) and len(result) != 0


print(is_valid("okay_ok1"))
