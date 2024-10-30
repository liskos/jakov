a = [int(x) for x in open("17data/17-328.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 50 == 0:
        b.append(a[x])

def f(x, v):
    n = x + v
    return n ** 0.5 == int(n ** 0.5)


for i in range(len(a) - 2):
    if (f(a[i],a[i+1]) and f(a[i+1],a[i+2]) and f(a[i],a[i+2])) and (min(a[i]+a[i+1],a[i+1] + a[i+2],a[i]+a[i+2]) > sum(b)/len(b)):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),min(r))