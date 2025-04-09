s = open("24data/k7-m22.txt").read()

k = 0
for i in range(len(s)-2):
    if int(s[i],17) > int(s[i+1],17) and int(s[i+1],17) > int(s[i+2],17):
        print(s[i])
        k += 1


print(k)