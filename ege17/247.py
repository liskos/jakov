a = [int(x) for x in open("17data/17-243.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 111 == 0:
        b.append(a[x])


def f(x):
    return x > max(b)
def d(x):
    return x % 10 == 7
for i in range(len(a) - 1):
    if f(a[i]) or f(a[i+1]) and (d(a[i]) or d(a[i+1])) :
        r.append(a[i] + a[i+1])

print(len(r), min(r))