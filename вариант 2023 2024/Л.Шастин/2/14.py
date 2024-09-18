for x in range(1,27):
    s1 = int("17035",27) + x * 27 ** 2
    s2 = x * 27 ** 4 + int("742m",27)
    s = s1 + s2 + x ** 3
    if s % 23 == 0:
        print(x,s // 23)
