a = [int(x) for x in open("17_17943.txt")]
r = []
b = len([x for x in a if abs(x) % 2 == 0])


for i in range(len(a)-1):
    if((a[i] > 0) == (a[i+1] > 0)) and abs(a[i] - a[i+1]) <= b:
        r.append(a[i] + a[i+1])

print(len(r),max(r))