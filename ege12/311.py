def f(s):
    while (">1" in s) or (">2" in s) or (">0" in s):
        if ">1" in s:
            s = s.replace(">1","20>",1)
        if ">2" in s:
            s = s.replace(">2","00>",1)
        if ">0" in s:
            s = s.replace(">0","10>",1)
    return s

for k in range(100,201):
    for m in range(100,201):
        for n in range(100,201):
            s = ">" + "0" * k + "1" * m + "2" * n
            a = f(s)
            a = a.replace(">","")
            if sum(map(int,a)) == 599:
                print(k)