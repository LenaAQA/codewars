# Есть массив с несколькими числами. Все числа равны, кроме одного. Попробуйте найти его!


# def find_uniq(arr):
#     arr = sorted(arr)
#     if arr[0] == arr[1]:
#         return arr[-1]
#     else:
#         return arr[0]

def find_uniq(arr):
    arr = sorted(arr)
    return arr[-1] if arr[0] == arr[1] else arr[0]


print(find_uniq([1, 1, 1, 2, 1, 1]))
