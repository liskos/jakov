def f(s):
    while "1111" in s:
            s = s.replace('1111',"2",1)
            s = s.replace('222','1',1)
    return s


print(f("1" * 46 + "2" * 31))
