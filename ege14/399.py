for p in range(2,100):
    for x in range(p):
        for y in range(p):
            n1 = 8 * p ** 3 + 7 * p ** 2 + x * p ** 1 + 6
            n2 = x * p ** 3 + 5 * p ** 2 + x * p ** 1 + 8
            r = y * p ** 4 + 7 * p ** 3 + y * p ** 2 + 9 * p ** 1 + 2
            if n1 + n2 == r:
                print(y * p ** 3 + x * p ** 2 + x * p ** 1 + y)