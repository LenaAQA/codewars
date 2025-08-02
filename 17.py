# DropCaps означает, что первая буква начального слова абзаца должна быть заглавной,
# а остальные — строчными, как в газете.


def drop_cap(words):
    for i in words.split():
        if len(i) > 2:
            words = words.replace(i, i.title())
    return words


print(drop_cap('apple'))
