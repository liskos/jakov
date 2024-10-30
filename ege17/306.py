a = [int(x) for x in open("17data/17-304.txt")]
r = []
b = []

def f(x,v):
    return (hex(x)[2:]).count("a") > 0 and (hex(x)[2:]).count("a") % 2 == 0

for i in range(len(a)-1):
    if f(a[i],a[i+1]) and (a[i]+a[i+1]) > sum(a)/len(a):
        r.append(a[i]+a[i+1])
print(len(r),min(r))
