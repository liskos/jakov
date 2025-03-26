for a in range(1,1000):
    if not all([(x & a == 0) and (x & 41 != 0) and (x & 33 == 0) for x in range(1,1000)]):
        print(a)