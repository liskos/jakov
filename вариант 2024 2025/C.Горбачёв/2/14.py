def pr(n):
    s = ""
    t = "01234"
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s

for x in range(1,1223):
    s = 4 ** x - 3 ** 331 + 9 ** 17
    if pr(s).count("0") == 77:
        print(x)