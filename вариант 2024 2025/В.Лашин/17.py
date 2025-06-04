a = [int(x) for x in open("17.txt")]
r = []
b = min(a)



for i in range(len(a)-1):
    if (a[i] % 43 == b) and (a[i+1] % 43 == b):
        r.append(abs(a[i]-a[i+1]))

print(len(r),max(r))