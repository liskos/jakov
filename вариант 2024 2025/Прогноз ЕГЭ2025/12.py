def f(s):
    while ("40" in s) or ("800" in s) or ("000" in s):
        if "40" in s:
            s = s.replace("40","0",1)
        if "800" in s:
            s = s.replace("800","04",1)
        if "000" in s:
            s = s.replace("000","8",1)
    return s

b = []
for i in range(4,10000):
    s = "4" + "0" * i
    if sum(map(int,f(s))) == 36:
        b.append(f(s))

print(max(b))