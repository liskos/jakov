import re
s = open("24data/24-191.txt").read()
numbers = r"[A][^AB]{15,}[A]"
k = 0
while re.search(numbers, s):
    s = s[re.search(numbers,s).end()-1:]
    k += 1
print(k)