def f(n):
    n = hex(n)[2:]
    if n % 2 == 0:
        b = b + '15'
    else:
        b = b + '0'
