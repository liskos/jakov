def f(s):
    while (">1" in s) or (">2" in s) or (">0" in s):
        if ">1" in s:
            s = s.replace(">1","22>",1)
        if ">2" in s:
            s = s.replace(">2","2>",1)
        if ">0" in s:
            s = s.replace(">0","1>",1)
    return s

for i in range(4,10000):
    s = ">" + "0" * 25 + "1" * i + "2" * 25
    d = f(s)
    d = d.replace(">","")
    if sum(map(int,d)) == 17:
        print(i)