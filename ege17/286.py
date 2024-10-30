a = [int(x) for x in open("17data/17-282.txt")]
r = []
b = []

for x in range(len(a)):
    if a[x] % 21 == 0:
        b.append(a[x])


def f(x):
    return sum(map(int,(oct(x)[2:]))) == sum(map(int,(oct(min(b))[2:])))

for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))