p = 0
for x in range(2,80):
    s1 =
    s2 = 7 * 100 ** 3 + x * 100 ** 2 + 2 * 100 + 5
    if (s1 + s2) % 11 == 0:
        p += 1
print(p)