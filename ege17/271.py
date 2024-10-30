a = [int(x) for x in open("17data/17-271.txt")]
b = []

sr = sum(a)/len(a)
for i in range(len(a)-1):
    if abs(a[i]) % 10 + abs(a[i+1]) % 10 == 7:
        b.append([a[i], a[i+1]])
r = max(x + y for x, y in b if x < sr and y < sr)
print(len(b),r)