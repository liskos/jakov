for a in range(1,1000):
    if all([not((x % a == 0) and (x % 12 == 0)) or ((x % 42 == 0) or (x % 12 != 0)) for x in range(1,1000)]):
        print(a)