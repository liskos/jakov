a = [int(x) for x in open("17data/17-301.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 12 == 0:
        b.append(sum(map(int,str(a[x]))))
def f(x,v,c):
    return x % (v + c) or v % (x + c) or c % (x + v)

for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) and (a[i] + a[i+1] + a[i+2]) < sum(b):
        r.append(a[i]+a[i+1]+a[i+2])
print(len(r),min(r))
