s = open("24data/24-j2.txt").read()
b = []
k = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        k += 1
    else:
        b.append(k)
        k = 1
print(s)
print(max(b))