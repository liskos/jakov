a = [int(x) for x in open("17data/17-299.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 50 == 0:
        b.append(sum(map(int,str(a[x]))))

def f(x,v,c):
    return x == sum(map(int,str(v))) or v == sum(map(int,str(c))) or x == sum(map(int,str(c)))


for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) and (a[i] + a[i+1] + a[i+2]) < sum(b):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))