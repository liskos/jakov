for x in range(0,10):
    n1 = 1 * int(f"1{x}324") ** 1 + 4
    n2 = int(f"13{x}42",24)
    if (n1 + n2) % 10 == 0:
        print((n1+n2)//10)