s = open("24data/k8-8.txt").read()
print(s)
k = 1
b = []
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        k += 1
    else:
        b.append(k)
        k = 1


print(max(b))