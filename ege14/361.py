p = 0
for y in range(2,10):
    for x in range(0,100):
        s1 = 1 * y ** 4 + 3 * y ** 3 + 1 * y ** 2 + 5 * y + 2
        s2 = 7 * 100 ** 3 + x * 100 ** 2 + 2 * 100 + 5
        if (s1 + s2) % 11 == 0:
            p += 1
print(p)