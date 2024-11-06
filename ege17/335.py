a = [int(x) for x in open("17data/17-335.txt")]
r = []
d = min([x for x in a if x % 43 == 0])

def f(x,y):
    return ((x + y) % d == 0) or (x % 10 == d % 10) or (y % 10 == d % 10)

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(max(a[i],a[i+1]))
print(len(r),max(r))
