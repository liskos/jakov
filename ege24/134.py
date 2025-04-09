s = open("24data/24-j3.txt").read()
b = []
k = 0
for i in range(len(s)-1):
    if s[i:i+3] == "TIK" or s[i:i+3] == "TOK":
        k += 1
print(k)