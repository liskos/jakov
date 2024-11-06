a = [int(x)for x in open("17data/17-339.txt")]
r = []
b = min(x for x in a if x > 0 and x % 19 == 0)




for i in range(len(a)-1):
    if a[i]+a[i+1] < b:
        r.append(abs(a[i]+a[i+1]))

print(len(r),max(r))