"""
Link: https://www.codewars.com/kata/56d31aaefd3a52902a000d66
"""


def rad_ladies(name):
    return "".join([i.upper() for i in name if i.isalpha() or i in " !"])


print(rad_ladies("k?%35a&&/y@@@£5599 m93753&$$$c$n///79u??@@%l?975$t?%5y%&$3$1!"))
