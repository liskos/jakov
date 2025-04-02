a = [int(x) for x in open("17_18257.txt")]
r = []
b = max(a)

for i in range(len(a)-1):
    if (i +1 + i + 2) % 10 == b % 10:
        r.append(abs((a[i]+a[i+1]) - (i+1 + i+2)))


print(len(r),min(r))