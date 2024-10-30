import operator
a = [int(x) for x in open("17data/17-296.txt")]
r = []
d = []
for x in range(len(a)):
    d.append(int(str(a[x])[-1]) + int(str(a[x])[-2]))
def f(c, b):

    return c * b > sum(d)

for i in range(len(a) - 1):
    if f(a[i], a[i + 1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))