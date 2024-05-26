def f(s):
    while ("1111" in s) or ("222" in s) or "33" in s:
        if "1111" in s:
            s = s.replace("111", "3", 1)
        else:
            if "222" in s:
                s = s.replace("222", "11", 1)
            else:
                s = s.replace("33","2",1)
    return s

a = set()
for i in range(1,1000):
    s = "1" * i
    a.add(f(s))
print(a,len(a))