def f(n):
    b = bin(n)[2:]
    if n % 2 == 0 and b.count('1') % 2 == 1:
        b = '1' + b
        print("11111")
    else:
        b = b + str(b.count('1') % 2)
        print("222")
    return int(b,2)

print(f(12))
print(f(4))