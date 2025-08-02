# Реализуйте String#digit?(на Java StringUtils.isDigit(String)),
# # который должен возвращать результат, trueесли заданный объект является
# # одной цифрой (0-9), falseв противном случае.


def is_digit(n):
    return len(n) == 1 and n.isdigit()


print(is_digit("a5"))
