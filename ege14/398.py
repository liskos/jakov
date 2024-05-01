for p in range(2,100):
    for x in range(p):
        for y in range(p):
            n1 = 5 * p ** 3 + x * p ** 2 + 8 * p ** 1 + 3
            n2 = x * p ** 3 + 9 * p ** 2 + x * p ** 1 + 9
            r = y * p ** 3 + 2 * p ** 2 + 0 * p ** 1 + y
            if n1 + n2 == r:
                print(x * p ** 3 + y * p ** 2 + y * p ** 1 + x)