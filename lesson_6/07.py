"""
Link: https://www.codewars.com/kata/563fb342f47611dae800003c
"""


def trim(phrase, size):
    if len(phrase) > size:
        if size > 3:
            return phrase[:size - 3] + "..."
        else:
            return phrase[:size] + "..."
    else:
        return phrase


print(trim("IBGWQ jT", 3))
