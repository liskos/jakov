def f(s):
    while "1111" in s:
            s = s.replace('1111',"7",1)
            s = s.replace('77','1',1)
    return s


print(f("1" * 95 + "7" * 31))
