def f(n):
    b = bin(n)[2:]
    if int(b) % 2 == 0:
        b += '10'
    else:
        b = '1' + '01'
    return int(b,2)
print(f(13))

