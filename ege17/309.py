a = [int(x) for x in open("17data/17-304.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 54 == 0:
        b.append(a[x])
def f(x,v):
    return

for i in range(len(a)-1):
    if f(a[i],a[i+1]) and (a[i]+a[i+1]) > sum(a)/len(a):
        r.append(a[i]+a[i+1])
print(len(r),min(r))
