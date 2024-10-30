a = [int(x) for x in open("17data/17-288.txt")]
r = []

def tr(n):
    n = abs(n)
    s = ""
    t = "0123456"
    if n == 0:
        return "0"
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s

def d(x, y, z, w):
    return tr(x)[-1] != "3" and tr(y)[-1] != "3" and tr(z)[-1] != "3" and tr(w)[-1] != "3"
def f(x, y, z , w):
    return abs(x) % 10 == 3 or abs(y) % 10 == 3 or abs(z) % 10 == 3 or abs(w) % 10 == 3

for i in range(len(a) - 3):
    if f(a[i], a[i + 1], a[i + 2], a[i + 3]) and d(a[i], a[i + 1], a[i + 2], a[i+3]):
        r.append(max(a[i], a[i + 1], a[i + 2]) - min(a[i], a[i + 1], a[i + 2]))

print(len(r), min(r))