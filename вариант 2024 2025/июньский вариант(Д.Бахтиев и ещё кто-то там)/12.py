def f(s):
    while ("33333" in s) or ("1111" in s):
        if "33333" in s:
            s = s.replace("33333","111",1)
        else:
            s = s.replace("111","33",1)
    return s

s = "3" * 234
print(f(s))
print(3**5)