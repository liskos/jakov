def chr(n):
    t = '0123'
    s = ''
    while n > 0:
        s = t[n%4] + s
        n //= 4
    return s