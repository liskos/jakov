s = open("24data/k7c-3.txt").read()
count = 0

for i in range(len(s)-2):
    if s[i+1] in "BDE" and s[i+2] in "ACD" and s[i] == s[i+2] and s[i+1] != s[i+2]:
        count += 1



print(count)