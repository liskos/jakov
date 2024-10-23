a = [int(x) for x in open("17data/17-7.txt")]
r = []

for i in range(len(a)-2):
    if (((hex(a[i])[2:])[0]).count("0") + ((hex(a[i+1])[2:])[0]).count("0") + ((hex(a[i+2])[2:])[0]).count("0")) > 1:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))