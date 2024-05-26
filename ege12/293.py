def f(s):
    while ("55555" in s):
        s = s.replace("55555", "88", 1)
        s = s.replace("888", "555", 1)
    return s


a = set()
for i in range(201,800):
    s = "5" * i
    print(f(s),i)
