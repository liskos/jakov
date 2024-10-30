import operator
a = [int(x) for x in open("17data/17-298.txt")]
r = []
d = []
for x in range(len(a)):
    if a[x] % 51 == 0:
        d.append(a[x])
def f(x):

    return (x) == (x % 10 * 51)

for i in range(len(a) - 1):
    if f(a[i]) != f(a[i+1]) and (a[i] + a[i+1]) < max(d):
        r.append(a[i]+a[i+1])

print(len(r),max(r))