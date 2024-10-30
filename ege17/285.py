a = [int(x) for x in open("17data/17-282.txt")]
r = []
b = []

for x in range(len(a)):
    if a[x] % 37 == 0:
        b.append(a[x])


def f(x):
    return sum(map(int,str(x))) == sum(map(int,str(min(b))))

for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))