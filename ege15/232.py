for a in range(1,1000):
    if all([not(not(x % 5490 == 0) and (x % a == 0) and (x % 6300 == 0)) or ((x % 5940 == 0) or (x % a != 0)) for x in range(1,1000)]):
        print(a)