a = [int(x)for x in open("17data/17-336.txt")]
r = []
b = max([x for x in a if x % 37 == 0])


def f(x,y):
    return (x % b == 0 or y % b == 0) and (x+y) % b > 30


for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))