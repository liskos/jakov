s = open("files/24_1__6anyf.txt").read()

import re

num = r"([1-9a-z][0-9a-z]*|0)"
pat = rf"{num}([-+*]{num})+"
b = [x.group() for x in re.finditer(pat,s)]
b = max(b,key=len)
print(len(b))