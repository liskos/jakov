for x in range(0,10):
    n1 = 2 * int(f"1{x}324") ** 1 + 7
    n2 = int(f"1{x}342",28)
    if (n2 - n1) % 25 == 0:
        print((n2-n1)//25)