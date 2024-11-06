a = [int(x) for x in open("17data/17-346.txt")]
r = []


def n(v):
    k = 1
    while v > 0:
        k *= v % 10
        v //= 10
    return k
def f(x, y, z):
    ym = n(x) * n(y) * n(z)
    return ym <= 2 * (10 ** 9) and str(ym)[0] == "5" and str(ym)[1] == "3" and str(ym)[2] == "7"


for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]):
        r.append(n(a[i]) * n(a[i+1]) * n(a[i+2]))

print(len(r),max(r))