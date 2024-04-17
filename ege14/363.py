for x in "0123456789abcdefghijklmno":
    s1 = f"1{x}23"
    s2 = f"32{x}1"
    s = int(s1, 44) - int(s2, 44)
    if s % 131 == 0:
        print(x, s // 131)
