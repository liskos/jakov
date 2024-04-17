for x in "0123456789abcdefghijklmno":
    for y in "0123456789a":
        s1 = f"7{y}23{x}5"
        s2 = f"67{x}9{y}"
        s = int(s1, 25) - int(s2, 11)
        if s  % 131 == 0:
            print(x,y, s // 131)
