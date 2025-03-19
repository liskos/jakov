for a in range(1, 1000):
    if all([(x % 18 != 0) or ((x % a == 0) or (x % 12 != 0)) for x in range(1, 1000)]):
        print(a)