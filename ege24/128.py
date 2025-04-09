s = open("24data/24-5.txt").read()

s = s.replace(")","B")
s = s.replace("()","(")
print(len,s.split("("))
print(max(map(len,s.split("("))))