for p in range(2,100):
    for x in range(p):
        for y in range(p):
            n1 = 3 * p ** 3 + 9 * p ** 2 + 7 * p ** 1 + x
            n2 = x * p ** 3 + 9 * p ** 2 + x * p ** 1 + 4
            r = y * p ** 3 + 1 * p ** 2 + 9 * p ** 1 + y
            if n1 + n2 == r:
                print(x * p ** 3 + x * p ** 2 + y * p ** 1 + y)