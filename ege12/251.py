def f(s):
    while "111" in s:
        s = s.replace("111","2",1)
        s = s.replace("2222","1",1)
    return s


m = min([f("1" * i).count("1") for i in range(81,1000)])
print([i for i in range(81,1000) if f("1" * i).count("1") == m][0])
