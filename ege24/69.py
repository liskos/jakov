s = open("24data/k8-96.txt").read()

print(s)
b = []
k = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        k += 1
    else:
        b.append([s[i],k])
        k = 1

print(*max(b,key=lambda x:x[-1]))