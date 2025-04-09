s = open("24data/k7-m24.txt").read()
k = 0
for i in range(len(s)-2):
    if int(s[i],20) >= int(s[i+1],20) and int(s[i+1],20) >= int(s[i+2],20):
        k += 1
        print(s[i])


print(k,5)