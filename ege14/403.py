for p in range(2,100):
    for y in range(p):
        for x in range(p):
            n1 = 3 * p ** 3 + 4 * p ** 2 + x * p ** 1 + 5
            n2 = x * p ** 3 + 9 * p ** 2 + x * p ** 1 + 3
            r = y * p ** 3 + y * p ** 2 + 6 * p ** 1 + 8
            if (n1 + n2) == r:
                print(y * p ** 3 + x * p ** 2 + x * p ** 1 + y)