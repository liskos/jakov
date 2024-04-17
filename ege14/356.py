for x in "0123456789abcdefg":
    s1 = f"131{x}1"
    s2 = f"13{x}3"
    s = int(s1, 15) + int(s2, 17)
    if s  % 11 == 0:
        print(x, s // 11)
