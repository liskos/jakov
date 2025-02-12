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
for i in range(4019,10**10+1,4019):
    if fnmatch.fnmatch(str(i),"1?359*0") and b.count(sum(map(int,str(i)))):
        print(i,i//4019)


# 193595230 48170
# 1035977630 257770
# 1135930160 282640
# 1335955790 332410
# 1835959580 456820
# 1935952300 481700