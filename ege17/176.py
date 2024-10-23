a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):
    if sum(map(int,str(a[i] % 100))) > 14 and a[i] % 3 != 0 and a[i] % 4 != 0 and a[i] % 7 != 0:
        r.append(a[i])
print(min(r),sum(r))