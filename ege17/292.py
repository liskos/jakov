a = [int(x) for x in open("17data/17-292.txt")]
r = []


def f(a, b):
    return (a % 6) + (b % 6) == (a % 11) + (b % 11)


for i in range(len(a) - 1):
    if f(a[i], a[i + 1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))