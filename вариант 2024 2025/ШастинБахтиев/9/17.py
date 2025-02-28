a = [int(x) for x in open("17 (4).txt")]
r = []
b = [x for x in a if len(str(abs(x))) == 4]



def f(x,y,z):
    i = int(len(str(abs(x)))==3)+int(len(str(abs(y)))==3)+int(len(str(abs(z)))==3)
    return i == 2
for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) and a[i] * a[i+1] * a[i+2] > sum(b):
        r.append(a[i]*a[i+1]*a[i+2])

print(len(r),abs(min(r)))