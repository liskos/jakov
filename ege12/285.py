def f(s):
    while ("555" in s) or ("888" in s):
        s = s.replace("555","8",1)
        s = s.replace("888","55",1)
    return s

for i in range(201,300):
    s = "8" * i
    if f(s).count("5") <f(s).count("8"):
        print(i,f(s))
