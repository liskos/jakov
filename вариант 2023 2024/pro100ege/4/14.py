
for x in "0123456789abcdefghi":
    s1 = f"78{x}79643"
    s2 = f"25{x}43"
    s3 = f"63{x}5"
    s = int(s1, 19) + int(s2, 19) + int(s3,19)
    if s % 18 == 0:
        print(x, s // 18)
368599039