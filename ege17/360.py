a = [int(x) for x in open("17data/17-360.txt")]
r = []
def n(v):
    k = 1
    while v > 0:
        k *= v % 10
        v //= 10
    return k
b = max(x for x in a if n(abs(x)) % 100 == 42)

def f(x,y,z):
    return (abs(x) == abs(y) and x != y) or (abs(y) == abs(z) and y != z) or (abs(x) == abs(z) and x != z) and x < b and y < b and z < b


for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]):
        if a[i] != a[i+1] and abs(a[i]) == abs(a[i+1]):
            r.append(a[i]*a[i+1])
        elif a[i] != a[i + 2] and abs(a[i]) == abs(a[i + 2]):
            r.append(a[i]*a[i+2])
        elif a[i+1] != a[i+2] and abs(a[i+1]) == abs(a[i+2]):
            r.append(a[i+1]*a[i+2])
print(len(r),abs(min(r)))
