for p in range(2,100):
    for x in range(p):
        for y in range(p):
            n1 = 8 * p ** 3 + 9 * p ** 2 + x * p ** 1 + 0
            n2 = x * p ** 3 + 6 * p ** 2 + x * p ** 1 + 4
            r = 1 * p ** 4 + y * p ** 3 + y * p ** 2 + 1 * p + 4
            if n1 + n2 == r:
                print(y * p ** 3 + x * p ** 2 + y * p ** 1 + x )