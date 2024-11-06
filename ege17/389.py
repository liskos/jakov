a = [int(x) for x in open("17data/17-388.txt")]
r = []
b = max([x for x in a if abs(x) % 100 == 68])
def f(x):
    return len(str(abs(x))) == 2



for i in range(len(a)-3):
    if (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2])) + int(f(a[i+3]))) == 1 or (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2])) + int(f(a[i+3]))) == 4 and (a[i] + a[i+1] + a[i+2] + a[i+3]) >= b:
        r.append(a[i]+a[i+1]+a[i+2]+a[i+3])

print(len(r),max(r))