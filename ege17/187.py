a = [int(x) for x in open("17data/17-6.txt")]
r = []

for i in range(len(a)-2):
    if (bin(a[i])[2:]).count("1") == 3 and (bin(a[i+1])[2:]).count("1") == 3 and (bin(a[i+2])[2:]).count("1") == 3:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))