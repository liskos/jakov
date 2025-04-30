# s = open("ycheba/Задача_2__fz2p__tadr.txt").read()
#
# t = ""
# k = 0
# for i in range(len(s)-2):
#     if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
#         k += 1
#
#
# print(k)

s = open("ycheba/1__1iafg (1).txt").read()
k = 0
t = ""
d = 0
m = 0
s = s.replace("BBC","+").replace("AAC","-")
print(s)
for i in range(len(s)):
    if s[i] == "+":
        k += 1
    elif s[i] == "-":
        d += 1
    else:
        k = 0
        d = 0
    m = max(m,d,k)


print(m)