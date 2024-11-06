a = [int(x) for x in open("17data/17-378.txt")]
r = []
b = max(x for x in a if abs(x) % 1001 == 0)

def f(x):
    return len(str(abs(x))) == 3

for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]) and a[i]+a[i+1] > b:
        r.append(a[i]+a[i+1])

print(len(r),max(r))