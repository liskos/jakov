a = [int(x) for x in open("17data/17-316.txt")]
r = []
b = []


def f(x, v):
    return (x + v) ** 0.5 == int((x + v)**0.5) and x + v > 0

for i in range(len(a) - 2):
    if f(a[i],a[i+1]) or f(a[i+1],a[i+2]) or f(a[i],a[i+2]) and (a[i] + a[i+1] + a[i+2]) / 3 > sum(a)/len(a):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))