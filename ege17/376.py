a = [int(x) for x in open("17data/17-376.txt")]
r = []
b = max(x for x in a if (hex(x)[2:])[-2:] == "0f")
def f(x):
    return x % 7 == 0

def d(x):
    return
for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]) and (a[i]+a[i+1]) % b:
        r.append(a[i]+a[i+1])

print(len(r),max(r))