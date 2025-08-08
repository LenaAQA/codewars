"""
https://www.codewars.com/kata/51f2b4448cadf20ed0000386
"""


def remove_url_anchor(url):
    return url[:url.index("#")] if "#" in url else url


print(remove_url_anchor("www.codewars.com#about"))
