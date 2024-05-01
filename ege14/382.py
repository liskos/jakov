for x in range(0,10):
    n1 = 1 * int(f"132{x}4") ** 1 + 3
    n2 = int(f"134{x}2",13)
    if (n1 - n2) % 30 == 0:
        print((n1-n2)//30)