def odinnac(n):
    while n > 0:
        if n % 11 == 2:
            return False
        n //= 11
    return True


for i in reversed(range(2031,14312+1)):
    if odinnac(i):
        print(i)
        break