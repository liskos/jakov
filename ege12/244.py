def f(s):
    while ("21" in s) or ("31" in s) or ("23" in s):
        if "21" in s:
            s = s.replace("21","12",1)
        if "31" in s:
            s = s.replace("31","13",1)
        if "23" in s: s = s.replace("23","32",1)
    return s


s = "1" * 50 + "2" * 50 + "3" * 50
b = ">" + "4" * 50
s = f(s)
b = f(b)
print(sum(map(int,s)),s[9],s[89],s[129])
