for a in range(1,1000):
    if all([not((x % a == 0) and not(x % 36 == 0)) or not(x % 12 == 0) for x in range(1,1000)]):
        print(a)