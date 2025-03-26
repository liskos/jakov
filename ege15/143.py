for a in range(1,1000):
    if all([not((x % 45 == 0) and not(x % 15 == 0)) or not(x % a == 0) for x in range(1,1000)]):
        print(a)