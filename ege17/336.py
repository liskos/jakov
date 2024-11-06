a = [int(x) for x in open("17data/17-336.txt")]
r = []
d = min([x for x in a if x % 8 == 0 and x != 8])

def f(x,y):
    return x % d == 0 and y % d == 0

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append([max(a[i],a[i+1]),a[i]+a[i+1]])
print(len(r),r)
