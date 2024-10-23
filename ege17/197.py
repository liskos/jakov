a = [int(x) for x in open("17data/17-10.txt")]
r = []

for i in range(len(a)-2):
    if len(str(a[i] + a[i+1] + a[i+2])) == 3 and (a[i] + a[i+1] + a[i+2]) % 10 > int((str(a[i] + a[i+1] + a[i+2]))[-2]):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),min(r))