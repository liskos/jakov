def f(s):
    while "111" in s:
        s = s.replace("111", "33", 1)
        s = s.replace("333", "1")
    return s

for n in range(1, 36):
    s = "1" * n
    if f(s) == "131":
        print(n,s)
