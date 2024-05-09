def f(s):
    while "111" in s:
        s = s.replace("111","22",1)
        s = s.replace("222","11",1)
    return s


m = 1000
for i in range(51,1000):
    s = "1" * i
    m = min(m, f(s).count("1"))
print(m)
for n in range(51,1000):
    s = "1" * n
    if f(s).count("1") == m:
        print(len(s))
        break
