def f(s):
    while "11" in s:
        if "112" in s:
            s = s.replace("112","7",1)
        else:
            s = s.replace("11","3",1)
    return s

for i in range(1, 30):
    s = "112" * 4 + "11" * (4)
    print(i, sum(map(int,f(s))), f(s))