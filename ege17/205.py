a = [int(x) for x in open("17data/17-205.txt")]
r = []


def f(x,y):
    return (x-y) % 2 == 0 and (x-y) % 37 == 0

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))