s = open("24data/k8-4.txt").read()

print(s)
b = []
k = 1
s += "b"
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        k += 1
    else:
        b.append([s[i],k])
        k = 1
print(len(s))
d = max(b,key=lambda x:x[-1])[1]
for x in b:
    if x[1] == d:
        print(x[0], x[1])