def f(s):
    while "111" in s:
        s = s.replace("111","2",1)
        s = s.replace("2222","11",1)
    return s

for i in range(80,150):
    s = "1" * i
    b = f(s)
    if b.count("1") == 1:
        print(len(s), b.count("1"))


