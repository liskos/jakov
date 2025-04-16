import re

s = open("24data/24-s1.txt").readlines()

number = r"A.R"
k = 0
for line in s:
    if re.search(number,line):
        k += 1
print(k)