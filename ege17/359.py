a = [int(x) for x in open("17data/17-354.txt")]
r = []

b = min(x for x in a if str(x)[-1] == "2")



def f(x,y):
    return abs(x) % 10 - abs(y) % 10 == 1
def d(x):
    return x % 5 == 0
for i in range(len(a)-1):
    if f(a[i],a[i+1]) and d(a[i]) != d(a[i+1]) and (a[i]**2)+(a[i+1]**2) > b ** 2:
        r.append((a[i]**2)+(a[i+1]**2))

print(len(r),min(r))