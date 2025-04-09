def f(s):
    while ("31" in s) or ("211" in s) or ("1111" in s):
        if "31" in s:
            s = s.replace("31","1",1)
        if "211" in s:
            s = s.replace("211","13",1)
        if "1111" in s:
            s = s.replace("1111","2",1)

    return s

b = []
for i in range(4,10000):
    s = "3" + "1" * i
    s = f(s)
    if sum(map(int,s)) == 15:
        b.append(i)
print(min(b))