def f(s):
    while "111" in s:
        s = s.replace("111","22",1)
        s = s.replace("222","11",1)
    return s

a = []
for i in range(71,1000):
    s = "1" * i
    a.append(f(s).count("1"))
print(max(a))
for i in range(71,1000):
    s = "1" * i
    if (len(f(s))) == 5:
        print(len(s))
        break

