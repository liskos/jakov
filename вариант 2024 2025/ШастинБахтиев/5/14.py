def sem(n):
    s = ""
    t = "0123456"
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s

for i in range(1,1000):
    s = 7 ** 666 + 7 ** 333 + 49 ** i - 343
    if sem(s).count("6") == 49:
        print(i)
