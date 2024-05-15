for x in range(32):
    for y in range(32):
        a = f"7{x}37{y}"
        b = f"9{y}63"
        c = f"15148"
        s = int(a,14) + int(b,14) + int(c,14)
        print(s,s//(x+y))
