def f(x):
    v = 0
    s = x // 1000 + x // 100 % 10
    s1 = x // 100 % 10 + x // 10 % 10
    s2 = x // 10 % 10 + x % 10
    mi = min(s1, s2, s)
    if s1 == mi:
        s, s2 = min(s, s2), max(s, s2)
        v = str(s) + str(s2)
    if s == mi:
        s1, s2 = min(s1, s2), max(s1, s2)
        v = str(s1) + str(s2)
    if s2 == mi:
        s, s1 = min(s, s1), max(s, s1)
        v = str(s) + str(s1)
    return v


for i in range(1000, 10000):
    if f(i) == '210':
        print(i)
        break

