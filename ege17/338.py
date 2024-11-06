a = [int(x)for x in open("17data/17-338.txt")]
r = []
b = min(a)

def f(x,y):
    return (x % 117 == b) or (y % 117 == b)


for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))