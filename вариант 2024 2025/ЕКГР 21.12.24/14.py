for x in range(25):
    s1 = 1 * 25 ** 7 + 1 * 25 ** 6 + 3 * 25 ** 5 + 5 * 25 ** 4 + 3 * 25 ** 3 + x * 25 ** 2 + 1 * 25 ** 1 + 2
    s2 = 1 * 25 ** 5 + 3 * 25 ** 4 + 5 * 25 ** 3 + x * 25 ** 2 + 2 * 25 + 1
    if (s1 + s2) % 24 == 0:
        print(x,(s1+s2)//24)