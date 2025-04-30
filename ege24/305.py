import re

s = open("24data/24-305.txt").read()

numbers = r"([0-9][1-9]*|0)"
numbers = rf"AF{numbers}([+*]{numbers})+"

b = [len(x.group()) for x in re.finditer(numbers,s)]

print(max(b))
