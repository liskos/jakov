for a in range(1,1000):
    if  all([((x-y) >= 39) or (y <= x) or (y >= (a - 20)) for x in range(1,1000) for y in range(1,1000)]):
        print(a)