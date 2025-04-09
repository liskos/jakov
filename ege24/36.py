s = open("24data/k7c-4.txt").read()

k = 0

for i in range(len(s)-2):
    if s[i] in "ADF" and s[i] != s[i+2] and s[i+2] in "CDF" and s[i+1] in "CDF" and s[i+1] != s[i+2]:
        k += 1

print(k)