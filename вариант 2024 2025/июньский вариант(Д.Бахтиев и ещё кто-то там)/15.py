for a in range(1,10000):
    if all([(x & 117 != 0) and not(x & 91 == 0) or not (x & a == 0) for x in range(1,1000)]):
        print(a)