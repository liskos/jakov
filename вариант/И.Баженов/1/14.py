for y in range(1,14):
    for x in range(0,11):
        s1 = int("230C",14) + y * 14 ** 4 + x * 14 ** 1
        s2 = int("A0910",11) + x * 11 ** 3
        if (s1 + s2) % 23 == 0:
            print(x+y,(s1+s2)//23)

