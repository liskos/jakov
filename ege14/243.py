a = int('25',8)
b = int('24',16)
c = int('43',8) - int('1B',16)
d = int('110101',2) + int('13',8)
x = 16**a + 4**b - 8**c - 2**d + 31
x = hex(x)[2:]
print(x)
print(x.count('0') + x.count('f'))