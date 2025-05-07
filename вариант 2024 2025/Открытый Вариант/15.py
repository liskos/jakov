b = set()
for a in range(1,10000):
    if all([not((x&52 != 0) and (x & 48 == 0)) or not(x&a==0) for x in range(1,1000)]):
        print(a)