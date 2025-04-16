k = 1000
t = ""
for s in open("24data/24-s1.txt"):
    if s.count("A") < k:
        k = s.count("A")
        t = s
d = []
for i in "QWERTYUIOPASDFGHJKLZXCVBNM":
    d.append([t.count(i), i])
d = sorted(d,key=lambda x:(x[0],x[1]), reverse=True)[0][-1]

s = [x.count(d) for x in open("24data/24-s1.txt")]
print(d,sum(s))




# print(s.count("J"))
# k = 0
# m = 1000
# b = 0
# d = ""
# for line in s:
#     if line.count("A") == 34:
#         m = line
#         break
# for i in m:
#     if m.count(i) > b:
#         b = m.count(i)
#         d = i
# print(b,d)

#J