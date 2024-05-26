def f(s):
    while ("33"  in s) or ("22"  in s) or ("11" in s):
        if "33" in s:
          s = s.replace("33","12",1)
        if "11" in s:
          s = s.replace("11","32",1)
        if "22" in s:
            s = s.replace("22", "31", 1)
    return s


s = "12" * 4 + "32" * 15 + "32" * 15 + "1" * 34
b = sum(map(int,s))
print(b,s)
