a = [int(x) for x in open("17data/17-304.txt")]
r = []
b = []

def f(x,v):
    return x % sum(map(int,oct(v)[2:])) == 0 or v % sum(map(int,oct(x)[2:])) == 0

for i in range(len(a)-1):
    if f(a[i],a[i+1]) and (a[i]+a[i+1]) % min(a) == 0:
        r.append(a[i]+a[i+1])
print(len(r),max(r))
