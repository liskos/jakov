for x in "0123456789abcdefghijklmno":
    s1 = int(f"a4{x}7f2",25)
    s2 = int(f"n{x}g5{x}h",25)
    s3 = int(f"74{x}m26",25)
    s = s1 + s2 + s3
    if s % 24 == 0:
        print(x,s//24)