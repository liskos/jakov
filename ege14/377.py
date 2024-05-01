for x in range(0,10):
    n1 = 1 * int(f"123{x}4") ** 2 + 3
    n2 = 1 * int(f"12{x}43") ** 2 + 2
    if (n1 + n2) % 50 == 0:
        print((n1+n2)//50)