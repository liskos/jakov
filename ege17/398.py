a = [int(x) for x in open("17data/17-390.txt")]
b = [x for x in a if abs(x) % 1000 == 151]
b = sum(b)/len(b)
r = []

def f(x):
    return len(str(abs(x))) == 4

def d(x):
    return (x) % 13 == 0
def c(x):
    return x % 7 == 0
def g(x,y,z):
    return x > b and y > b and z > b

for i in range(len(a)-2):
    if 3 > (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2]))) > 0 and (int(d(a[i])) + int(d(a[i+1])) + int(d(a[i+2]))) > (int(c(a[i])) + int(c(a[i+1])) + int(c(a[i+2]))) and g(a[i],a[i+1],a[i+2]):
        r.append(a[i]+a[i+1]+a[i+2])


print(len(r),min(r))