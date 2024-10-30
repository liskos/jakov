def f(s):
    while ("002" in s) or ("22" in s):
        if "002" in s:
            s = s.replace("002","44",1)
        if "222" in s:
            s = s.replace("222","2",1)
    return s

a = []
for i in range(4,10000):
    s = "0" + ("2" * i)
    if sum(map(int,(f(s)))) == 42:
        print(i)