def f(s):
    while "111" in s or "22" in s:
        s = s.replace("111","2",1)
        s = s.replace("222","1",1)
        s = s.replace("221","1",1)
        s = s.replace("122","1",1)
        s = s.replace("22","22",1)
    return s


