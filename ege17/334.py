a = [int(x) for x in open("17data/17-1.txt")]
r = []
d = [x for x in a if x % 15 == 0 and x > 0]
print(d)

def f(x,y):
    return x % 2 !=0 and y % 2 != 0 and (x+y)/2 >= min(d)

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append((a[i]+a[i+1])/2)
print(len(r),min(r))
