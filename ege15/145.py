for a in range(1,1000):
    if all([not((x % 34 == 0) and not(x % 51 == 0)) or (not(x % a == 0) or (x % 51 == 0)) for x in range(1,1000)]):
        print(a)