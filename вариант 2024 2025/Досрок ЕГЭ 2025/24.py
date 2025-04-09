s = open("24_21421.txt").read()
k = ""
b = []
kol = 0
for i in range(len(s)):
    if s[i].isdigit():
        k = k + s[i]
        kol += 1
    elif k == "":
        pass
    else:
        b.append([int(k,36),kol])
        k = ""
        kol = 0

print(max([x[0] for x in b if x[0] % 2 == 0]))