a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if str(a[i]).count("0") > 1 and a[i] % 7 == 0:
        r.append(a[i])
print(max(r),len(r))