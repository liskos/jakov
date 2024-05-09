def f(s):
    while "21" in s:
        s = s.replace("21", "6", 1)
    return s

for n in range(1, 10):
    s = "21" * n + (10 - n) * "1"
    if sum(map(int,f(s))) == 50:
        print(n,s)
