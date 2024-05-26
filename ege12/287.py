def f(s):
    while ("555" in s) or ("888" in s):
        s = s.replace("555","8",1)
        s = s.replace("888","55",1)
    return s

for i in range(301,500):
    s = "8" * i
    if f(s).count("5")==1 and f(s).count("8") == 1:
        print(i,f(s))
