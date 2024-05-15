def f(s):
    while "111" in s:
        s = s.replace("111","2",1)
        s = s.replace("2222","333",1)
        s = s.replace("33","1",1)
    return s
a = []
for i in range(101,1000):
    s = "1" * i
    a.append(f(s).count("1"))
m = min(a)
for i in range(101,1000):
    s = "1" * i
    if f(s).count("1") == m:
        print(len(s))
        break
