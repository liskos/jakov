def f(a,b):
    global m
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1,b)+f(a+3,b)+f(m[a-1],b)

def fib():
    m = [1,1]
    for _ in range(30):
        m.append(m[-1]+m[-2])
    return m

m = fib()
print(f(6,21))
