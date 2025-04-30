a = [int(x) for x in open("17_18582.txt")]

b = min(a)
r = []


for i in range(len(a)-2):
    if (int(a[i] < 0) + int(a[i+1] < 0) + int(a[i+2] < 0)) >= 2 and str(a[i]+a[i+1]+a[i+2])[-1] == str(b)[-1]:
        r.append(abs(a[i]+a[i+1]+a[i+2]))

print(len(r),max(r),(b,r))