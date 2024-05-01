for x in range(0,10):
    n1 = 1 * int(f"132{x}4") ** 1 + 3
    n2 = int(f"13{x}42",22)
    if abs(n1 - n2) % 100 == 53:
        print(abs(n1-n2)//100)