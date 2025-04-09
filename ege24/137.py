s = open("24data/24-s1.txt").read()
b = []
k = 0
for i in range(len(s)-1):
    if s[i:i+3] == "OCK" and s[i-1] != "T" and s[i-2] != "S":
        k += 1
print(k)