a = [int(x) for x in open("17data/17-288.txt")]
r = []

def tr(n):
    s = ""
    t = "0123456"
    if n == 0:
        return "0"
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s

def d(x, y, z):
    return x < 0 or y < 0 or z < 0

def f(x, y, z):
    return tr(abs(x))[-1] != tr(abs(y))[-1] and tr(abs(x))[-1] != tr(abs(z))[-1]

for i in range(len(a) - 2):
    if f(a[i], a[i + 1], a[i + 2]) and d(a[i], a[i + 1], a[i + 2]):
        r.append(max(a[i], a[i + 1], a[i + 2]) - min(a[i], a[i + 1], a[i + 2]))

print(len(r), min(r))