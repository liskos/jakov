for a in range(1,1000):
    if all([not(not(x % a == 0) and (x % 21 == 0)) or not(x % 14 == 0) for x in range(1,1000)]):
        print(a)