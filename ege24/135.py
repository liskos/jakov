s = open("24data/24-j4.txt").read()
b = []
k = 0
for i in range(1,len(s)-1):
    if s[i-1] != "J" and s[i:i+4] == "BOSS" and s[i+4] != "J":
        k += 1
print(k)