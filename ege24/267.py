s = open("24data/24-264.txt").read()
import re
numbers = r"([123456789abcdef][0123456789abcdef])+"

b = [len(x.group()) for x in re.finditer(numbers,s)]
print(max(b))
t = ""
m = 0
for i in s:
    if t and t[0] != "0" and i in "0123456789abcdef":
        t += i
        m = max(m,len(t))
    else:
        t = i
print(m)