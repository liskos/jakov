s = open("files/1__1iafg (4).txt").read()
s = s.replace("BBC","1").replace("AAC","2")
k = 0
d = 0
m = 0
for i in s:
    if i == "1" or i == 2:
        m += 1
        k = max(m,k)
    else:
        m = 0
print(k)