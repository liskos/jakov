a = [int(x) for x in open('17_12249.txt')]
b = [x for x in a if len(str(abs(x))) == 5 and str(x)[-1] == "3"]
r = []

def f(x,y,z):
    return str(x)[-1] == "3" or str(y)[-1] == "3" or str(z)[-1] == "3"


for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) and (a[i]+ a[i+1] + a[i+2]) <= max(b):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))