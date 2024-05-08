def f(s):
    while "111" in s:
            s = s.replace('111',"22",1)
            s = s.replace('2222','1',1)
    return s


print(f("1" * 63 + "2" * 61))
