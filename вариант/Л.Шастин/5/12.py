def f(s):
    while ("72" in s) or ("522" in s) or ("2222" in s):
        if "72" in s:
            s = s.replace("72","2",1)
        if "522" in s:
            s = s.replace("522","27",1)
        if "2222" in s:
            s = s.replace("2222","5",1)
    return s

for i in range(4,10000):
    s = "5" + "2" * i
    if sum(map(int,f(s))) == 22:
        print(i)