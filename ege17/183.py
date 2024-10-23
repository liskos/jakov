a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if (hex(a[i])[2:])[-1] == "b" and (a[i] % 7 == 0 and a[i] % 6 != 0 and a[i] % 13 != 0 and a[i] % 19 != 0):
        r.append(a[i])
print(sum(r),len(r))