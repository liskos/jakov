a = [int(x) for x in open("17data/17-328.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 50 == 0:
        b.append(a[x])

def f(x, v):
    n = x + v
    return str(n) == str(n)[::-1]


for i in range(len(a) - 2):
    if (f(a[i],a[i+1]) and f(a[i+1],a[i+2]) and f(a[i],a[i+2])) and (max(a[i]+a[i+1],a[i+1] + a[i+2],a[i]+a[i+2]) < max(b)):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))