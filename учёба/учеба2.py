import re
s = open("24.txt").read()
num = r"[1-9AB][0-9AB]+[13579B]"

b = max((x.group() for x in re.finditer(num,s)),key=lambda x:int(x,12))
print(s.find(b))
#