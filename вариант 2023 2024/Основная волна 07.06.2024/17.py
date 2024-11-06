a = [int(x) for x in open("17_17530.txt")]
r = []


for i in range(len(a)-1):
    if (abs(a[i])) % 55 == min(a) or (abs(a[i+1])) % 55 == min(a):
        r.append(a[i]+a[i+1])

print(len(r),min(r))