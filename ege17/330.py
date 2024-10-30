a = [int(x) for x in open("17data/17-328.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 22 == 0:
        b.append(sum(map(int,str(a[x]))))

def f(x, v):
    n = x + v
    return oct(n)[2:] not in "1357"


for i in range(len(a) - 2):
    if (f(a[i],a[i+1]) and f(a[i+1],a[i+2]) and f(a[i],a[i+2])) and ((a[i]+a[i+1]+a[i+2])  < sum(b)):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),min(r))