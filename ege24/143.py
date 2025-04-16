import re

s = open("24data/24-s1.txt").readlines()

number = r"Z.RO"
k = 0
for i in s:
    if re.search(number,i):
        k += 1


print(k)