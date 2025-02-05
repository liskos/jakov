def f(n):
    b = bin(n)[2:]
    if b[-1] == "0":
        b = "1" + b + "00"
    else:
        b += bin(sum(map(int,b)))[2:]
    return int(b,2)

print(f(4),f(13))


for i in range(1,10000):
    if f(i) > 205:
        print(i,f(i))