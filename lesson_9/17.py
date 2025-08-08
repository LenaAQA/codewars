"""
Link: https://www.codewars.com/kata/552e45cc30b0dbd01100001a
"""


def zipvalidate(postcode):
    return len(postcode) == 6 and postcode[0] not in "05789" and postcode.isdigit()


print(zipvalidate('198328'))
