"""
Link: https://www.codewars.com/kata/56c30eaef85696bf35000ccf
"""


def christmas_tree(height):
    if height < 3:
        return ""
    segments = height // 3
    tree_lines = []
    max_width = 1 + 2 * (segments + 1)
    for seg in range(segments):
        for i in range(3):
            stars = 1 + 2 * (i + seg)
            line = ' ' * ((max_width - stars) // 2) + '*' * stars
            tree_lines.append(line)
    trunk = ' ' * ((max_width - 3) // 2) + '###'
    tree_lines.append(trunk)
    return '\r\n'.join(tree_lines)


print(christmas_tree(5))
