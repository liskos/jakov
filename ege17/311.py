a = [int(x) for x in open("17data/17-304.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 120 == 0:
        b.append(a[x])
def f(x):
    return (hex(x)[2:]).count("a") > 0 and (hex(x)[2:]).count("a") % 2 == 0

for i in range(len(a)-1):
    if f(a[i]) and f(a[i+1]) and (a[i]+a[i+1]) > max(b):
        r.append(a[i]+a[i+1])
print(len(r),min(r))
