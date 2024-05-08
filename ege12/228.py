def f(s):
    while "15" in s:
        s = s.replace("15","8",1)
    return s

for i in range(1, 15):
    s = "15" * i + "5" * (15-i)
    print(i, sum(map(int,f(s))), f(s))