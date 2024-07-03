def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 10 or a == 15:
        return 0
    return f(a+3,b)+f(a*3,b)


s = set()
for i in range(1,100):
    if f(3,i) % 2 == 0 and f(3,i) < 100:
        s.add(f(3,i))
print(len(s))


