def f(s):
    while ("13" in s) or ("32" in s) or ("12" in s):
        if "13" in s:
            s = s.replace("13","31",1)
        if "32" in s:
            s = s.replace("32","23",1)
        if "12" in s: s = s.replace("12","21",1)
    return s


s = "1" * 50 + "2" * 50 + "3" * 50
b = ">" + "4" * 50
s = f(s)
b = f(b)
print(sum(map(int,s)),s[9],s[69],s[140])
