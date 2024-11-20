a = [int(x) for x in open("17_16328.txt")]
r = min([x for x in a if x % 19 == 0])
b = []


def f(x):
    return x % r

for i in range(len(a)-1):
    if f(a[i]) or f(a[i]):
        b.append(a[i]+a[i+1])

print(len(b),max(b))