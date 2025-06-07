import re
s = open("24_20968.txt").read()

num = r"([1-9][0-9]*[02468]|0)"
patt = rf"{num}([+*]{num})+"

b = max([x.group() for x in re.finditer(patt,s)],key=len)

print(len(b))