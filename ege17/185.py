a = [int(x) for x in open("17data/17-5.txt")]
r = []

for i in range(len(a)-1):
    if abs(a[i]) % 10 == 7 or abs(a[i+1]) % 10 == 7:
        r.append(a[i]+a[i+1])

print(len(r),max(r))