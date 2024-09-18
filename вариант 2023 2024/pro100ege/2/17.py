a = [int(i) for i in open("17.txt")]
m = max([x for x in a if str(abs(x))[0] == "8"])
rez = []
for i in range(len(a)-2):
    z = a[i:i+3]
    c = [x for x in z if str(abs(x))[0] == "6"]
    if len(c) <= 1 and sum(z) >= m:
        rez.append(sum(z))
print(len(rez), min(rez))