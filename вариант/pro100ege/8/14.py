def f(n):
    t = "0123456789abcdefghijklmno"
    s = ""
    while n>0:
        s = t[n%25]+ s
        n //= 25
    return s

s = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
b = f(s)
b = b.replace("0","")
b = b.replace("1","")
b = b.replace("2","")

print(len(b))