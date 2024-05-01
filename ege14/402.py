for p in range(2,100):
    for y in range(p):
        for x in range(p):
            n1 = 1 * p ** 3 + x * p ** 2 + 7 * p ** 1 + 7
            n2 = x * p ** 3 + x * p ** 2 + 7 * p ** 1 + 7
            r = y * p ** 3 + 0 * p ** 2 + y * p ** 1 + y
            if (n1 + n2) == r:
                print(y * p ** 3 + x * p ** 2 + y * p ** 1 + x)