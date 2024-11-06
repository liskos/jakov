a = [int(x) for x in open("17data/17-370.txt")]
r = []
b = min(x for x in a if x % 2 == 0)
def f(x):
    return x % 2 == 0

def d(x):
    return
for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]) and :
        r.append(a[i]+a[i+1])

print(len(r),min(r))