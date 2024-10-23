a = [int(x) for x in open("17data/17-3.txt")]
r = []

for i in range(len(a)-2):
    z = a[i] * a[i+1] * a[i+2]
    x = a[i] + a[i+1] + a[i+2]
    if z % 7 == 0 and str(x)[-1] == "5":
        r.append(x)

print(len(r),max(r))