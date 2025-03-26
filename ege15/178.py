for a in range(1,1000):
    if all([(x & 19 == 0) and (x & 38 != 0) or (not(x & 43 == 0) or ((x & a == 0) and (x & 43 == 0))) for x in range(1,1000)]):
        print(a)