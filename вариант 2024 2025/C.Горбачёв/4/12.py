def f(s):
    while (">3" in s) or (">2" in s) or (">0" in s):
        if ">3" in s:
            s = s.replace(">3","22>",1)
        if ">2" in s:
            s = s.replace(">2","2>",1)
        if ">0" in s:
            s = s.replace(">0","3>",1)
    return s
for n in range(1,100):
    s = ">" + "0" * 17 + "3" * n + "2" * 17
    r = f(s)
    r = r[:-1]
    ss = sum(map(int,r))
    if int(ss**0.5)**2 == ss:
        print(n, ss )