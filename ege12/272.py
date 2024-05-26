def f(s):
    while ("12" in s) or ("13" in s):
        s = s.replace("12","21",1)
        s = s.replace("31","23",1)
        s = s.replace("13","23",1)
    return s

a = []
for i in range(1,404):
    for g in range(1,140):
        s = "1" * i + "3" * g
        if sum(map(int,f(s))) == 404:
            a.append(len(s))
print(max(a))