def f(s):
    while "1111" in s:
        s = s.replace("111","22",1)
        s = s.replace("222","11",1)
    return s

for i in range(70,100):
    s = "1" * i
    b = f(s)
    if b.count("1") >= 5:
        print(len(s), b.count("1"))


