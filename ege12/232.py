def f(s):
    while "11" in s:
        if "112" in s:
            s = s.replace("112","7",1)
        else:
            s = s.replace("11","3",1)
    return s


s = "112" * 4 + "1" * 4
print(sum(map(int,f(s))), f(s))