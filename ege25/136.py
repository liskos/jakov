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


b = prost(1)
def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    pr = [x for x in a if b.count(x)]
    if len(pr) > 5:
        return True,max(pr)
    else:
        return False


for n in range(25317,51237+1):
    if delitel(n):
        print(n,delitel(n)[1])


# 30030 13
# 39270 17
# 43890 19
# 46410 17


