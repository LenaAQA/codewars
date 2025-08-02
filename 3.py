# Есть массив строк. Все строки содержат одинаковые буквы , кроме одной. Попробуйте найти её!

from collections import Counter


def find_uniq(arr):
    def norm(s):
        return ''.join(sorted(set(s.replace(' ', '').lower())))

    normalized = list(map(norm, arr))
    freq = Counter(normalized)
    unique_key = next(k for k, v in freq.items() if v == 1)
    return arr[normalized.index(unique_key)]


print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
