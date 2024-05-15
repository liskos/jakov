def f(s):
    while "1111" in s:
        s = s.replace("1111","2",1)
        s = s.replace("22","11",1)
    return s

a = []
for i in range(101,1000):
    s = "1" * i
    a.append(f(s).count("1"))
m = min(a)
for i in range(101,1000):
    s = "1" * i
    if f(s).count("1")== m:
        print(len(s))
        break


