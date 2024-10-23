a = [int(x) for x in open("17data/17-3.txt")]
r = []

for i in range(len(a)-1):
    b = (a[i] + a[i+1])
    v = (a[i] * a[i + 1])
    if (b % 3 == 0 and b % 6 != 0 and (str(v)[-1]) == "8") :
        r.append(a[i] + a[i+1])
print(len(r),max(r))