"""
Link: https://www.codewars.com/kata/585a36b445376cbc22000072
"""


def area_code(text):
    return text[text.index("(") + 1:text.index(")")]


print(area_code("The supplier's phone number is (555) 867-5309"))
