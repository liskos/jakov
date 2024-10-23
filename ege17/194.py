a = [int(x) for x in open("17data/17-9.txt")]
r = []

for i in range(len(a)-2):
    b = bin(a[i])[2:].count("1")
    b1 = bin(a[i])[2:].count("0")
    v = bin(a[i+1])[2:].count("1")
    v1 = bin(a[i+1])[2:].count("0")
    c = bin(a[i+2])[2:].count("1")
    c1 = bin(a[i+2])[2:].count("0")
    if ((b == 2 and b1 > 0) and (v == 2 and v1 > 0)) or ((b == 2 and b1 > 0) and (c == 2 and c1 > 0)) or ((v == 2 and v1 > 0) and (c == 2 and c1 > 0)):
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r),max(r))