a = [int(x) for x in open("17data/17-354.txt")]

b = [x for x in a if len(str(abs(x))) > 1 and str(x)[-2] == str(x)[-1]]

r = []

def f(x, y):
    return str(x)[-1] == str(y)[-2]

def g(x):
    return x % 11 == 0

for i in range(len(a) - 1):
    if len(str(abs(a[i + 1]))) > 1:
        if (f(a[i], a[i + 1]) or f(a[i + 1], a[i])) and g(a[i]) != g(a[i + 1]) and (a[i] ** 2) + (a[i + 1] ** 2) >= (sum(b) / len(b)) ** 2:
            r.append((a[i] ** 2) + (a[i + 1] ** 2))

print(len(r), max(r))
