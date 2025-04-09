s = open("24data/k7-m22.txt").read()

k = 0
for i in range(len(s)-2):
    if s[i] > s[i+1] > s[i+2]:
        print(i)
        k += 1


print(k)