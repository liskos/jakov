def f(n):
    b = bin(n)[2:]
    if int(b) % 2 == 0:
        b += '10'
    else:
        b = '1' + b + '01'
    return int(b,2)
print(f(13))


for i in range(1,10000):
    if f(i) > 516:
        print(i)
        break
