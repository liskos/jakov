s = open("24data/24-305.txt").read()
import re
num = r"([1-9][0-9]*|0)"
number = rf"AF{num}([+*]{num})+"
b = [len(x.group()) for x in re.finditer(number,s)]
print(max(b))