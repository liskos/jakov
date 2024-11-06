a = [int(x)for x in open("17data/17-340.txt")]
r = []
b = (x for x in a if x % 22 == 0)
b = sum(b)/len(a)

def f(x,y):
    c = int(oct(x)[2:])
    return (x + y) < b

for i in range(len(a)-1):
    if a[i]+a[i+1] < b:
        r.append(abs(a[i]+a[i+1]))

print(len(r),max(r))