def g(n):
    t = "0123456789abcdefghijklmnopq"
    s = ""
    while n>0:
        s = t[n%27] + s
        n //= 27
    return s

s = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024

