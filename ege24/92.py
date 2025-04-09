s = open("24data/24-1.txt").read()

b = []
k = ""
for i in range(len(s)):
    if s[i].isdigit() and int(s[i],36) % 2 == 0:
        k += s[i]
    elif k == "":
        pass
    else:
        b.append(int(k))
        k = ""



print(max(b))