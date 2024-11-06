a = [int(x) for x in open("17data/17-385.txt")]
r = []
b = []
def f(x):
    return len(str(x)) == 2
for x in range(len(a)):
    if sum(map(int,str(a[x]))) == 4:
        b.append(a[x])



for i in range(len(a)-1):
    if min(a[i],a[i+1]) > max(b):
        r.append(sum(map(int,str(a[i])))+sum(map(int,str(a[i+1]))))

print(len(r),max(r))