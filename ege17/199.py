a = [int(x) for x in open("17data/17-199.txt")]
r = []

def f(x):
    return 10<=x<=99 and x%2 == 0

for i in range(len(a)-2):
    if not(f(a[i])) and f(a[i+1]) and not(f(a[i+2])):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))