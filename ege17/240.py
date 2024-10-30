a = [int(x) for x in open("17data/17-1.txt")]
r = []

average = sum(a) / len(a)


def f(x):
    return x < average
def d(x):
    return str(x).count("6") > 0
for i in range(len(a) - 2):
    if (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2]))) > 1 and (int(d(a[i])) + int(d(a[i+1])) + int(d(a[i+2]))) > 0:
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))