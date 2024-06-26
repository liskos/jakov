v = []
a = [int(i) for i in open("17.txt")]
m50 = max(i for i in a if abs(i) % 100 == 50)
for i in range(len(a)-2):
    z = a[i:i+3]
    if len(set(z)) == 3 and len([x for x in z if 10000 <= abs(x) < 100000]) == 3 and sum(z) <= m50:
        v.append(sum(z))
print(len(v),max(v))


