def f(n):
    b = bin(n)[2:]
    if b.count('1') > b.count('0'):
        b = b + '0'
    else:
        b = b + '1'
