s = open("files/24_2__6anzj.txt").read()

import re

num = r"([1-7][0-7]*|0)"
pat = rf"{num}([+*]{num})+"
b = [x.group() for x in re.finditer(pat,s)]
b = max(b,key=len)
print(len(b))