for a in range(1,1000):
    if all([not((x % a == 0) and (x % 15 != 0)) or (x % 18 == 0) or (x % 15 == 0) for x in range(1,1000)]):
        print(a)