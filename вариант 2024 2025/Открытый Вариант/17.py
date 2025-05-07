a = [int(x) for x in open("17_21903.txt")]
b = [x for x in a if abs(x) % 100 == 15 and len(str(abs(x))) == 3]
r = []


for i in range(len(a)-2):
    if ((a[i] < 0) == (a[i+1] < 0)) and ((a[i+1] < 0) == (a[i+2] < 0)) and min(a[i],a[i+1],a[i+2]) * max(a[i],a[i+1],a[i+2]) > min(b) ** 2:
        r.append((min(a[i],a[i+1],a[i+2])) * (max(a[i],a[i+1],a[i+2])))

print(len(r),min(r))