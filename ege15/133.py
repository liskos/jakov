for a in range(1,1000):
    if all([not((x % 40 == 0) or (x % 64 == 0)) or (x % a == 0) for x in range(1,1000)]):
        print(a)