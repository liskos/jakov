a = [int(x) for x in open("17data/17-380.txt")]
r = []
b = max(x for x in a if abs(x) % 100 == 25)


def d(x):
    return len(str(abs(x))) == 4
for i in range(len(a)-2):
    if (int(d(a[i])) + int(d(a[i+1])) + int(d(a[i+2]))) < 3 and a[i]+a[i+1]+a[i+2] <= b:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))