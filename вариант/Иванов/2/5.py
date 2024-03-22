def f(n):
    n = bin(n)[2:]
    if n.count('1') + n.count('0') % 2 != 0:
        if n[len(n)//2-1] == '0':
            n = n[:len(n) // 2] + '1' + n[len(n) // 2 + 1:]
        else:
            n = n[:len(n) // 2] + '0' + n[len(n) // 2 + 1:]
    else:
        inverted_num = binary_num[:center - 1] + ('0' if binary_num[center - 1] == '1' else '1') + (
            '0' if binary_num[center] == '1' else '1') + binary_num[center + 1:]