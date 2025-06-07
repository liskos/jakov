import re

s = open("files/24_1__6ba37.txt").read()

num = r"([1-6][0-6]*|0)"
pattern = rf"{num}([+*]{num})*"

b = max([x.group() for x in re.finditer(pattern,s)],key=len)
print(b)
print(len(b))
