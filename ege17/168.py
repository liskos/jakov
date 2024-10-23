a = [int(x) for x in open("17data/17-3.txt")]
r = []

for i in range(len(a)-3):

    if a[i] > a[i+1] and a[i+1] > a[i+2] and a[i+2] > a[i+3] and a[i] - a[+3] > 1000:
        r.append(a[i]+a[i+1]+a[i+2]+a[i+3])
print(len(r),min(r))