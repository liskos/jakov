a = [int(x) for x in open("17data/17-345.txt")]
r = []
b = [x for x in a if x % 100 == 52]


def f(x):
    return x < max(b) - min(b)

for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))