a = [int(x) for x in open("17data/17-290.txt")]
r = []

def tr(n):
    s = ""
    t = "01234"
    if n == 0:
        return "0"
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s
def ch(n):
    s = ""
    t = "012345"
    if n == 0:
        return "0"
    while n > 0:
        s = t[n % 6] + s
        n //= 6
    return s
def d(x, y, z):
    return len(ch(x)) == 4 and len(ch(y)) == 4 and len(ch(z)) == 4

def f(x, y, z):
    return tr(x)[-1] == "1" or tr(y)[-1] == "1" or tr(z)[-1] == "1"

for i in range(len(a) - 2):
    if f(a[i], a[i + 1], a[i + 2]) and d(a[i], a[i + 1], a[i + 2]):
        r.append(max(a[i], a[i + 1], a[i + 2]) - min(a[i], a[i + 1], a[i + 2]))

print(len(r), min(r))