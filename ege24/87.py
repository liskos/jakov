s = open("24data/24-1.txt").read()

b = []
k = ""
for i in range(len(s)-1):
    if s[i].isdigit():
       k += s[i]
    elif k == "":
        pass

    else:
        b.append(int(k))
        k = ""

print(max(x for x in b if x % 2 != 0))