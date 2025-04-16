s = open("24data/24-5.txt").read()
#
# k = 0
# for i in range(len(s)):
#     if s[i] == "(" and k == 10000:
#         print(i)
#     if s[i] == "(":
#         k += 1
k = 0
s = s.replace("(","0",9999)

while s[0] != "(":
    k += 1
    s = s[1:]

print(k)