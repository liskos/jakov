a = [int(x) for x in open("17data/17-1.txt")]
r = []

average = sum(a) / len(a)


def f(x):
    return x > average
for i in range(len(a) - 2):
    if f(a[i]) or f(a[i+1]) or f(a[i+2]):
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))