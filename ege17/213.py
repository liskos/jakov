a = [int(x) for x in open("17data/17-1.txt")]
r = []

average = sum(a) / len(a)

def f(x):
    return x > average

for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % 100 == 31 and (f(a[i]) and f(a[i+1])):
        r.append(a[i] + a[i+1])

print(len(r), max(r))