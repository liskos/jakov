def f(s):
    while ("90" in s) or ("300" in s) or ("000" in s):
        if "90" in s:
            s = s.replace("90","0",1)
        if "300" in s:
            s = s.replace("300","09",1)
        if "000" in s:
            s = s.replace("000","3",1)
    return s


k = 0
for i in range(4,10000):
    s = "9" + "0" * i
    if f(s).count("9") == 2:
        k += 1
print(k)