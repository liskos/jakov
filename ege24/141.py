import re

s = open("24data/24-s1.txt").readlines()

pattern = r'F.O'  # F, любой символ, O

k = 0
for line in s:
    if re.search(pattern, line):
        k += 1

print(k)
