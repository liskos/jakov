s = open("24data/24-5.txt").read()
k = 0
s = s.replace("()","0",9999)
print(s.find("()"))
# while s[0] != "()":
#     k += 1
#     s = s[1:]
#
# print(k)