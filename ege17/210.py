a = [int(x) for x in open("17data/17-1.txt")]
r = []


def f(x):
    return x > sum(a)/len(a)

for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))