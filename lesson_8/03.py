"""
Link: https://www.codewars.com/kata/54b724efac3d5402db00065e
"""


from preloaded import MORSE_CODE


def decode_morse(morse_code):
    s = []
    for i in morse_code.split("   "):
        w = ""
        for ii in i.split():
            w += MORSE_CODE[ii]
        s.append(w)
    return " ".join(s).strip()


print(decode_morse('.-'))
