a = [int(x) for x in open("17data/17-3.txt")]
r = []

for i in range(len(a)-2):

    if a[i] < a[i+1] < a[i+2]:
        r.append(a[i+2] - a[i])
print(len(r),min(r))