def d(n):
    t = "0123456789abcdefghijklmno"
    s = ""
    while n > 0:
        s = t[n%25]+s
        n //= 25
    return s

s = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
s = d(s)
s = s.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("a","")
print(len(s))