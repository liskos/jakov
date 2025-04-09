s = open("24data/k7c-1.txt").read()
i = 0
count = 0

while i < len(s) - 2:
    if s[i] in "BCD" and s[i+1] in "BDE" and s[i] != s[i+1] and s[i+2] in "BCE" and s[i+1] != s[i+2]:
        count += 1

print(count)
