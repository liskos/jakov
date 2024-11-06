a = [int(x) for x in open("17data/17-352.txt")]
r = []
b = max(x for x in a if x % 73 == 0)



for i in range(len(a)-1):
    if a[i] >= b and a[i+1] >= b:
        r.append(a[i]+a[i+1])

print(len(r),max(r))
