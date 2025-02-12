def prosto(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = False
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000)if a[i]]
    return r
b = prosto(1)
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)

    pr = [x for x in a if b.count(x)]
    if len(pr) != 0:
        return len(a),max(pr)
    else:
        return 0,2


for i in range(1000000,10000000):
    if delitel(i)[0] == 1600:
        print(i,delitel(i)[1])