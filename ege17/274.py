a = [int(x) for x in open("17data/17-274.txt")]
r = []


def f(v,b):
    return (abs(v) + abs(b)) > 17043 and  (abs(v) + abs(b)) % 3 == 0

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))