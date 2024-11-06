a = [int(x) for x in open("17data/17-366.txt")]
r = []
b = [x for x in a if abs(x) % 100 == 68]


def f(x):
    return abs(x) % 100 == 68

for i in range(len(a)-1):
    if f(a[i])!=f(a[i+1]) and (a[i]**2) + (a[i+1]**2) >= min(b)**2:
        r.append(a[i]+a[i+1])

print(len(r),max(r))