a = [int(x) for x in open("17_22230.txt")]
d = max([c for c in a if c % 25 == 0])
r = []
b = min([x for x in a if x > 0 and x % 10 == 8])
print(d)
def f(x):
    return len(str(abs(x))) == 4
for i in range(len(a)-2):
    if (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2]))) == 2 and ((abs(a[i]) % b == 0) or (abs(a[i+1]) % b == 0) or (abs(a[i+2]) % b == 0)) and (a[i] + a[i+1] + a[i+2]) >= d:
        r.append(a[i]+a[i+1]+a[i+2])
        print(a[i],a[i+1],a[i+2])
print(len(r),max(r))