a = [int(x) for x in open("17data/17-273.txt")]
r = []
b = []



def f(x,b,c):
    return (x + b + c) < max(a)


for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]):
        r.append(min(a[i],a[i+1],a[i+2])+max(a[i],a[i+1],a[i+2]))

print(len(r),sum(r))