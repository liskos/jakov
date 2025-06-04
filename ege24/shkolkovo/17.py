import re
s = open("files/Задание_24__t7r1.txt").read()

num = "[02468]*|[13579]*"

b = [x.group() for x in re.finditer(num,s)]
b = sorted(b,key=len)[-1]
print(b)
print(len(b))