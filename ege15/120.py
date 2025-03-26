for a in range(1,1000):
    if all([not(not(x % a == 0) and (x % 6 == 0)) or not(x % 3 == 0) for x in range(1,1000)]):
        print(a)
