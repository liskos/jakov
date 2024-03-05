b = 10111110
b = str(b)
b = b[:7]
print(b)


n = 101
n = bin(n)[2:]
b = n = n.replace('0','8')
a = '5'
b = b.replace([0],a)

print(b)

b = '10111'
b = b[:-2]
print(b)

def f(n):
    n = bin(n)[2:]
    b = str(n)
    n = str(n) + b[-2]
    n = str(n) + b[1]
    print(n)
print(f(16))