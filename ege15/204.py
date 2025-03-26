for a in range(50,120+1):
    if all([not(x & a == 0) or (not(x & 31 != 0) or (x & 35 != 0)) for x in range(1,1000)]):
        print(a)