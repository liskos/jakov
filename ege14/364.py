p = 0
for x in range(55):
    for y in range(55):
        for z in range(55):
            for a in range(55):
                s1 = z * 55 ** 3 + a * 55 ** 2 + y * 55 ** 1 + x
                s2 = 2 * 55 ** 3 + x * 55 ** 2 + a * 55 ** 1 + y
                if (s1-s2) % 29 == 0:
                    print(a,(s1 - s2) // 29)
                if a > p:
                    p = a
print(p)

