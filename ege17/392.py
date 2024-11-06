a = [int(x) for x in open("17data/17-390.txt")]
b = [x for x in a if abs(x) % 100 == 38]
b = sum(b)/len(b)
r = []

def f(x):
    return len(str(abs(x))) == 3

def d(x):
    return abs(x) % 10 == 3

def g(x,y,z):
    return x < b and y < b and z < b


for i in range(len(a)-2):
    if (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2]))) > 1 and (int(d(a[i])) + int(d(a[i+1])) + int(d(a[i+2]))) == 1 and g(a[i],a[i+1],a[i+2]):
        r.append(a[i]+a[i+1]+a[i+2])


print(len(r),max(r))