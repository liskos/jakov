a = [int(x) for x in open("LpSdeR1bC.txt")]
b = [x for x in a if x % 10 == 8]
r = []

for i in range(len(a)-1):
    if (a[i] % 16 == min(b)) != (a[i+1] % 16 == min(b)):
        r.append(a[i] + a[i+1])

print(len(r),max(r))