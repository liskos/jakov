def f(s):
    while "1111" in s:
        s = s.replace("1111","2",1)
        s = s.replace("22","11",1)
    return s

for i in range(184,210):
    s = "1" * i
    b = f(s)
    if b.count("1") >= 3:
        print(len(s), b.count("1"))


