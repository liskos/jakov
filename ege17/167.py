a = [int(x) for x in open("17data/17-3.txt")]
r = []

for i in range(len(a)-3):

    if (a[i] % 2 == 0 and a[i+1] % 2 != 0) or (a[i] % 2 != 0 and a[i+1] % 2 == 0) and (a[i+1] % 2 == 0 and a[i+2] % 2 != 0) or (a[i+1] % 2 != 0 and a[i+2] % 2 == 0) and (a[i+2] % 2 != 0 and a[i+3] % 2 == 0) or (a[i+2] % 2 == 0 and a[i+3] % 2 != 0):
        r.append(a[i]+a[i+1]+a[i+2]+a[i+3])
print(len(r),max(r))