def f(s):
    while "!1" in s or "!2" in s or "!0" in s:
        if "1" in s:
            s = s.replace("!1","2!",1)
        if "!2" in s:
            s = s.replace("!2,30!",1)
        if "!0" in s:
            s = s.replace("!0","1!",1)
    return s

for i in range(1,1000):
    s = "!" + "0" * 15 + "1" * i + "19" * 2
    if f(i)