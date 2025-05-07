s = open("kege/24_20968 (1).txt").read()


import re
num = r"([1-9][0-9]*[02468]|0)"
num = rf"{num}([+*]{num})+"

b = [len(x.group()) for x in re.finditer(num,s)]

print(max(b))