def tr(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n //= 4
    return s


a = set()
for x in range(0,10000):
    s = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 4 ** x - 2022
    t = tr(s)
    a.add(sum(map(int,t)))
    if x % 100 == 0:
        print(len(a))
print(len(a))