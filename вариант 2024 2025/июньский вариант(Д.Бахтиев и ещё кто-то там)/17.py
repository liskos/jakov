a = [int(x) for x in open("17.txt")]
r = []
b = sum(a) / len(a)

for i in range(len(a)-1):
    if abs(a[i] + a[i+1]) > b:
        r.append(a[i]+a[i+1])

print(len(r),abs(min(r)))