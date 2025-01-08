a = [int(x) for x in open("17_19249.txt")]

b = max(x for x in a if len(str(abs(x))) == 5 and abs(x) % 100 == 43)
r = []

def f(x,y,z):
    return (len(str(abs(x))) == 5 and abs(x) % 100 == 43) or (len(str(abs(y))) == 5 and abs(y) % 100 == 43) or (len(str(abs(z))) == 5 and abs(z) % 100 == 43)


for i in range(len(a)-2):
    if f(a[i-1],a[i],a[i+1]) and ((a[i-1] ** 2) + (a[i] ** 2) + (a[i+1] ** 2)) <= b ** 2:
        r.append((a[i-1] ** 2) + (a[i] ** 2) + (a[i+1] ** 2))

print(len(r),min(r))