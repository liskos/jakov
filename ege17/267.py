a = [int(x) for x in open("17data/17-243.txt")]
r = []
b = [(sum(map(int,str(x)))) for x in a if x % 49 == 0]


def f(x, y):
    return x < sum(b) and y >= sum(b) and y % 13 == 0
for i in range(len(a)-1):
    if f(a[i],a[i+1]) or f(a[i+1],a[i]):
        r.append(a[i]+a[i+1])

print(len(r),max(r),r)