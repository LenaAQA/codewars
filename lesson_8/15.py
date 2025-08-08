"""
Link: https://www.codewars.com/kata/596343a24489a8b2a00000a2
"""


def is_it_a_num(s: str) -> str:
    st = "".join([i for i in s if i.isdigit()])
    if len(st) == 11 and st[0] == "0":
        return st
    else:
        return "Not a phone number"


print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))
