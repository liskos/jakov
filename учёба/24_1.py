s = open("ycheba/6__2pp78.txt").read()
m = 0
t = ""
d = 0
k = 0
s = s.replace("YZX","+").replace("ZXY","-")
for i in range(len(s)):
    if s[i] == "+":
        k += 1
    elif s[i] == "-":
        d += 1
    else:
        k = 0
        d = 0
    m = max(m,k,d)

print(m)

# s = open("ycheba/9__2pp7k.txt").read()
# t = ""
# m = 0
# for i in range(len(s)):
#     if s[i] in "AEIOUY" and (s[-1] not in "AEIOUY" or not t):
#         t += s[i]
#     elif t and t[-1] in "AEIOUY" and s[i] not in "AEIOUY":
#         t += s[i]
#     else:
#         t = ""
#     m = max(m,len(t))
#
# print(m)