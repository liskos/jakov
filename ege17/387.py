a = [int(x) for x in open("17data/17-387.txt")]
r = []
b = []
def f(x):
    return abs(x) % 100 == 13



for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))