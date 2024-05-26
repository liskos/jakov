def f(s):
    while ("555" in s) or ("888" in s):
        s = s.replace("555","8",1)
        s = s.replace("888","55",1)
    return s


for i in range(101,250):
    s = "5" * i
    if "8" not in (f(s)):
        print(f(s),i,"@@",len(s))