a = [int(x) for x in open("17data/17-275.txt")]
r = []


def f(v,b):
    return (v + b) % 11 == 0

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))