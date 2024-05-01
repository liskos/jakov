for x in range(0,10):
    n1 = 2 * int(f"1{x}324") ** 1 + 3
    n2 = int(f"134{x}2",22)
    if abs(n1 - n2) % 50 == 31:
        print(abs(n1-n2)//50)