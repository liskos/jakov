a = [int(x) for x in open("17data/17-379.txt")]
r = []
b = max(x for x in a if abs(x) % 100 == 15)

def f(x):
    return len(str(abs(x))) == 4

for i in range(len(a)-2):
    if (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2]))) == 1 and (a[i]+a[i+1]+a[i+2]) >= b:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))