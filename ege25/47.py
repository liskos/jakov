def prost(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = False
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000) if a[i]]
    return r


p = 0
b = prost(1)
for n in range(4730727,4730818):
    if b.count(n):
        p += 1
        print(p,n)

# 1 4730729
# 2 4730771
# 3 4730779
# 4 4730807
# 5 4730809
# 6 4730813
