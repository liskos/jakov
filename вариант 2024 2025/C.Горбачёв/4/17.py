a = [int(x) for x in open("17_18257.txt")]
r = []
b = max(a)

for i in range(len(a)-1):
    if (i + i + 1) % 10 == b % 10:
        r.append(abs(a[i]-a[i+1]))


print(len(r),min(r))