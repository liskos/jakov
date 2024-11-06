a = [int(x) for x in open("17data/17-377.txt")]
r = []
b = max(x for x in a if abs(x) % 17 == 0)



for i in range(len(a)-1):
    if (a[i]+a[i+1]) > b:
        r.append(a[i]+a[i+1])

print(len(r),max(r))