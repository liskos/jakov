import re
s = open("24_19149.txt").read()
num = r"([1-4]{1,}[0-4]*)"
num = rf"[(]{num}([+]{1}{num})*[)]"
b = [(x.group()) for x in re.finditer(num,s)]
d = [c for c in b if eval(c) % 2 == 0]
print(d)
print(len(max(d,key=len)))