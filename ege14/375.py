for x in range(0,10):
    n1 = 1 * int(f"123{x}4") ** 2 + 1
    n2 = 1 * int(f"1{x}243") ** 2 + 2 * int(f"1{x}243") + 3
    if (n1 + n2) % 25 == 0:
        print((n1+n2)//25)