"""
Link: https://www.codewars.com/kata/599cf86d01a4108584000064
"""


def length_of_railway(sounds):
    i = 0
    speed_state = 0
    total = 0
    while i < len(sounds):
        if sounds[i:i+3] == "呜呜呜":
            speed_state += 1
            i += 3
        elif sounds[i:i+2] == "哐当":
            if speed_state % 2 == 1:
                total += 20
            else:
                total += 10
            i += 2
        else:
            i += 1
    return total


print(length_of_railway('呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当'))
