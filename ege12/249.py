def f(s):
    while "1111" in s:
        s = s.replace("1111","2",1)
        s = s.replace("22","11",1)
    return s

for i in range(100,150):
    s = "1" * i
    b = f(s)
    if b.count("1") == 1:
        print(len(s), b.count("1"))


