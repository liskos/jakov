a = [int(x) for x in open("17_16383.txt")]
d = [x for x in a if (str(abs(x)))[-2:] == "21" and len(str(abs(x))) == 5]
r = []
def f(x):
    return (str(abs(x)))[-2:] == "21" and len(str(abs(x))) == 5
for i in range(len(a)-1):
    if a[i] != a[i+1] and (a[i] ** 2)+ (a[i+1] ** 2) >= max(d)**2:
        r.append(a[i]+a[i+1])

print(len(r),max(r))

