def f(s):
    while (">1" in s) or (">2" in s) or (">3" in s):
        if ">1" in s:
            s = s.replace(">1","22>",1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">3" in s:
            s = s.replace(">3", "1>", 1)
    return s

s = ">" + "1" * 26 + "2" * 10 + "3" * 14
s = f(s)
s = s.replace(">","")
print(sum(map(int,s)))