a = [int(x) for x in open("5PjNh0D16-.txt")]
r = []
b = [x for x in a if x > 0 and len(str(x)) == 4 and x % 10 == 6]

for i in range(len(a)-2):
    t = a[i:i+3]
    t1 = [x for x in t if len(str(abs(x)))==4 and abs(x)% 10 == 6]
    if len(t1) == 1 and sum(t) <= min(b):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r),r)