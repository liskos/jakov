import fnmatch
def prost(n):
    a = [True] * 100000
    a[0] = False
    a[1] = False
    for i in range(2,100000):
        if a[i]:
            for g in range(i**2,100000,i):
                a[g] = False
    r = [i for i in range(100000)if a[i]]
    return r

b = prost(1231)
for i in range(311,10**8+1,311):
    if fnmatch.fnmatch(str(i),"12?5*5??") and b.count(sum(map(int,str(i)))):
        print(i,i//311)