def f(s):
    while ("12" in s) or ("322" in s) or ("222" in s):
        if "12" in s:
            s = s.replace("12","2",1)
        if "322" in s:
            s = s.replace("322","21",1)
        if "222" in s:
            s = s.replace("222","3",1)
    return s


a = []
for i in range(4,10000):
    s = "1" + "2" * i
    if sum(map(int,f(s))) == 15:
        a.append(i)

print(min(a))
