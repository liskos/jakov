import re
s = open("files/24-1__63h3j.txt").read()

num = r"([1-9][0-9]*|0)"
pat = rf"?[-]{num}([-+]{num})+"

b = [x.group() for x in re.finditer(pat,s)]
b = max(b,key=len)
print(len(b))
