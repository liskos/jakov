def f(s):
    while "13" in s:
        s = s.replace("13","5",1)
    return s

for i in range(1, 15):
    s = "13" * i + "3" * (15-i)
    print(i, sum(map(int,f(s))), f(s))