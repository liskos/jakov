for x in range(0,10):
    n1 = 1 * int(f"12{x}34") ** 2 + 1
    n2 = 1 * int(f"124{x}3") ** 2 + 1 * int(f"124{x}3") + 1
    if (n1 + n2) % 30 == 0:
        print((n1+n2)//30)