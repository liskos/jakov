for a in range(1,1000):
    if all([not((x % a == 0) and not(x % 50 == 0)) or (not(x % 18 == 0) or (x % 50 == 0)) for x in range(1,1000)]):
        print(a)