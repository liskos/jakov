def p(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s

for x in range(1,100):
    s = 4 * 625 ** 1920 + 4 * 125 ** x - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
    a = p(s)
    if a.count("0") == 1891:
        print(x,a)