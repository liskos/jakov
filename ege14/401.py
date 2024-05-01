for p in range(2,100):
    for x in range(p):
        for y in range(p):
            n1 = 4 * p ** 3 + x * p ** 2 + 4 * p + 6
            n2 = x * p ** 3 + x * p ** 2 + 1 * p + 7
            r = y * p ** 4 + 3 * p ** 3 + 8 * p ** 2 + 6 * p ** 1 + y
            if (n1 + n2) == r:
                print(x * p ** 3 + y * p ** 2 + x * p + y)
