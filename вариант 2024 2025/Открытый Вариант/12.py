def f(s):
    while ("19" in s) or ("399" in s) or ("999" in s):
        if "19" in s:
            s = s.replace("19","9",1)
        if "399" in s:
            s = s.replace("399","91",1)
        if "999" in s:
            s = s.replace("999","3",1)

    return s


for i in range(4,10000):
    s = "1" + "9" * i
    if sum(map(int,f(s))) == 33:
        print(i)