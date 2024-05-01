for p in range(2,100):
    for x in range(p):
        for y in range(p):
            n1 = 5 * p ** 3 + x * p ** 2 + 1 * p ** 1 + 6
            n2 = x * p ** 3 + x * p ** 2 + x * p ** 1 + 5
            r = 1 * p ** 4 + 1 * p ** 3 + 5 * p ** 2 + y * p ** 1 + y
            if n1 + n2 == r:
                print(y * p ** 2 + x * p ** 1 + y)