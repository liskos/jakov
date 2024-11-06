a = [int(x) for x in open("17data/17-354.txt")]
r = []

b = min(x for x in a if str(x)[-1] == "3")



def f(x):
    return str(x)[-1] == "3"

for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]) and (a[i]**2)+(a[i+1]**2) < b ** 2:
        r.append((a[i]**2)+(a[i+1]**2))

print(len(r),max(r))