def prost(n):
    a = [True] * 200000
    a[0] = False
    a[1] = False
    for i in range(2,200000):
        if a[i]:
            for g in range(i**2,200000,i):
                a[g] = True
    r = [i for i in range(200000) if a[i]]
    return r



for i in range(125697,190234+1):
    