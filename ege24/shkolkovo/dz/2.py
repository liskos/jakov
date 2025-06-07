import re

s = open("files/24_2__6jwgo.txt").read()

num = r"[1-9][0-9]*"
pattern = rf"{num}([-*]{num})*"

b = max([x.group() for x in re.finditer(pattern,s)],key=len)
print(b)
print(eval(b))