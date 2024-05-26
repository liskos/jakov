def f(s):
    while ("5555" in s):
        s = s.replace("5555", "8", 1)
        s = s.replace("88", "5", 1)
    return s


a = set()
for i in range(301,800):
    s = "5" * i
    print(f(s),i)
