for x in "0123456789abcdefghi":
    s1 = f"98897{x}21"
    s2 = f"2{x}923"
    s = int(s1,19) + int(s2,19)
    if s % 18 == 0:
        print(x,s//18)