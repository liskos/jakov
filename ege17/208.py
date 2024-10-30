a = [int(x) for x in open("17data/17-205.txt")]
r = []


def f(x):
    return abs(x) % 100 == 17

for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]) and (a[i]+a[i+1]) % 2 == 0:
        r.append(a[i]+a[i+1])

print(len(r),max(r))