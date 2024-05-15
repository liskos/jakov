def f(s):
    while "53" in s:
        s = s.replace("53","8",1)
    return s

for i in range(1, 30):
    s = "53" * 11 + "5" * (i-11)
    print(i, sum(map(int,f(s))), f(s))