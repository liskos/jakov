a = [int(x) for x in open("17data/17-243.txt")]
r = []
b = []

for x in range(len(a)):
    if a[x] % 35 == 0:
        b.append(sum(map(int,str(a[x]))))

def f(x,y):
    return x > sum(b) and y <= sum(b) and hex(y)[2:][-2:] == "ef"
for i in range(len(a)-1):
    if f(a[i],a[i+1]) or f(a[i+1],a[i]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))