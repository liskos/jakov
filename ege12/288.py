def f(s):
    while ("555" in s) or ("888" in s):
        s = s.replace("555","8",1)
        s = s.replace("888","55",1)
    return s


a = set()
for i in range(2,500):
    s = "8" * i
    a.add(f(s))
print(len(a))
