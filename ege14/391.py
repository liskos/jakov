for x in range(0,37):
    for m in range(0,37):
        for f in range(0,37):
            for t in range(0,37):
                for y in range(0,37):
                    s1 = m * 30 ** 4 + f * 30 ** 3 + x * 30 ** 2 + 7 * 30 + 2
                    s2 = t * 30 ** 4 + x * 30 ** 3 + 7 * 30 ** 2 + y * 30 + 2
                    if (s1 + s2) % 536 == 0:
                        print(x,(s1+s2)//536)