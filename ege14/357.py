for x in "0123456789abcde":
    for y in "0123456789abcdefg":
        s1 = f"123{x}5"
        s2 = f"67{y}9"
        s = int(s1, 15) + int(s2, 17)
        if s  % 131 == 0:
            print(x,y, s // 131)
