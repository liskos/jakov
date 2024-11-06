a = [int(x) for x in open("17data/17-344.txt")]
r = []
b = min(x for x in a if x % 103 == 0)



def f(x,y):
    return (x + y) % 2 == 0 and abs(x-y) % b == 0

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))