for x in range(109):
        s1 = x * 109 ** 3 + 7 * 109 ** 2 + 5 * 109 ** 1 + 1
        s2 = 2 * 215 ** 3 + 3 * 215 ** 2 + 7 * 215 ** 1 + x
        if (s1 + s2) % 567 == 0:
            print((s1 + s2)//567)

