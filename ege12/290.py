def f(s):
    while ("55555" in s):
        s = s.replace("55555", "88", 1)
        s = s.replace("888", "55", 1)
    return s


a = []
for i in range(301,800):
    s = "5" * i
    a.append([f(s).count("5"), i])
print(max(a,key=lambda x:x[0]))