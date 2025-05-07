import re,string
s = open("24data/24-307.txt").read()

numbers = r"([1-9][0-9]*|0)"
numbers = rf"{numbers}([+*]{numbers})+B"

b = [len(x.group()) for x in re.finditer(numbers,s)]
print(max(b))
