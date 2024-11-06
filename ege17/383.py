a = [int(x) for x in open("17data/17-383.txt")]
r = []
def d(x):
    return len(str(abs(x))) == 2
b = max(x for x in a if d(x) == True)



for i in range(len(a)-1):
    if (d(a[i]) or d(a[i+1])) and (a[i]+a[i+1]) <= b**2:
        r.append(a[i]+a[i+1])

print(len(r),max(r))