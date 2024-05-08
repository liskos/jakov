def f(s):
    while "111" in s or "222" in s:
            s = s.replace('111',"2",1)
            s = s.replace('222','1',1)
    return s


print(f("1" * 2018 + "2" * 2019))
