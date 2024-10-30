a = [int(x) for x in open("17data/17-257.txt")]
r = []
b = []

for x in range(len(a)):
    if a[x] % 2 != 0:
        b.append(a[x])

def f(x):
    return (2*x) > max(b)

for i in range(len(a)-1):
    if f(a[i]+a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))