s = open("kege/24_21717 (1).txt").read()
#
# k = 0
# m = 100000
# l = 0
# for r in range(len(s)):
#     if s[r:r+3] == "RSQ":
#         k += 1
#     while k >= 130:
#         if s[l:l+3] == "RSQ":
#             k -= 1
#         l += 1
#     if k == 129:
#         if s[l-1:l+2] == "RSQ":
#             k += 1
#             l -= 1
#     while r+3 < len(s) and s[r+2] == "Q":
#         r += 1
#     if k == 130:
#         m = min(m,r-l+3)
#
# print(m)
# m = 10000
# ind = [x for x in range(len(s)) if s[x:x+3] == "RSQ"]
# try:
#     for i in range(len(ind)):
#         l = ind[i]
#         r = ind[i+129] + 3
#         while s[r] == "Q":
#             r += 1
#         m = min(m,r-l+1)
# except:
#     pass
# print(m)
# n = 10**10
# ind = [x for x in range(len(s)) if s[x:x+3] == "RSQ"]
# import re
# num = r"RSQ(.*RSQ){129}[Q]*[^Q]"
# for i in ind:
#     d = s[i:]
#     n = min(len(re.match(num,d).group()),n)
#
#
# print(n)
import fnmatch
for i in range(1000):
    if fnmatch.fnmatch(str(i), "1*[!07]"):
        print(i)