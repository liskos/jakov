for x in range(0,10):
    n1 = 2 * int(f"13{x}24") ** 1 + 6
    n2 = int(f"134{x}2",19)
    if (n1 + n2) % 15 == 0:
        print((n1+n2)//15)