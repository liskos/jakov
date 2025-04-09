a = [int(x) for x in open("17.txt")]
r = []
b = [x for x in a if x < 0]



for i in range(len(a)-2):
    if min(a[i],a[i+1],a[i+2]) * max(a[i],a[i+1],a[i+2]) > sum(b):
 ##       r.append(abs(a[i]+a[i+1]+a[i+2]))
          r.append(a[i]+a[i+1]+a[i+2])

print(len(r),abs(max(r)),sum(b),r)