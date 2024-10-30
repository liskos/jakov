a = [int(x) for x in open("17data/17-316.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 202 == 0:
        b.append(a[x])

def f(x, v):
    return x % 2 == 0 and v % 2 == 0 and (x+v) % 100 == 44
def d(x):
    return sum(map(int,str(x)))
for i in range(len(a) - 2):
    if f(a[i],a[i+1]) or f(a[i+1],a[i+2]) or f(a[i],a[i+2]) and (d(a[i]) + d(a[i+1]) + d(a[i+2])) > max(b):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),min(r))