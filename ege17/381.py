a = [int(x) for x in open("17data/17-381.txt")]
r = []
def d(x):
    return len(str(abs(x))) == 4
b = max(x for x in a if abs(x) % 100 == 39 and d(x) == True)



for i in range(len(a)-2):
    if (int(d(a[i])) + int(d(a[i+1])) + int(d(a[i+2]))) == 1 and (a[i]+a[i+1]+a[i+2])**2 <= b**2:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))