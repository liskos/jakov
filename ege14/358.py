for x in "0123456789abcdefghijkl":
    for y in "0123456789abc":
        s1 = f"{x}23{x}5"
        s2 = f"67{y}9{y}"
        s = int(s1, 22) - int(s2, 13)
        if s  % 57 == 0:
            print(x,y, s // 57)
