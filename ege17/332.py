a = [int(x) for x in open("17data/17-332.txt")]
r = []
b = []
c = []
for x in range(len(a)):
    if a[x] % 17 == 0:
        b.append(a[x])

def f(x, v):
    return sum(map(int,str(x))) == sum(map(int,str(v)))


for i in range(len(a) - 2):
    if (f(a[i],a[i+2])) and (a[i+1] < sum(b)/len(b)):
        r.append(sum(int(digit) for digit in str(a[i+1])))
for x in range(len(r)):
    if r.count(a[x]) > 1:
        c.append([a[x],r.count(a[x])])

print(len(r),max(r),c)