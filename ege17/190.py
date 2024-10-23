a = [int(x) for x in open("17data/17-7.txt")]
r = []

for i in range(len(a)):
    if (oct(a[i])[2:])[-1] == "7" and (oct(a[i])[2:])[-2:] != "27":
        r.append(a[i])

print(len(r),max(r))