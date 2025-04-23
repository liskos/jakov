a = [int(x) for x in open("5PjNh0D16-.txt")]
r = []
b = [x for x in a if x > 0 and len(str(x)) == 4 and x % 10 == 6]


def f(x,y,z):
    return (int(abs(x) % 10 == 6) + int(abs(y) % 10 == 6) + int(abs(z) % 10 == 6)) == 1
for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) and a[i] + a[i+1] + a[i+2] <= min(b):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r),r)