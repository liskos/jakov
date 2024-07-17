def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0

    return f(a+3,b)+f(a*3,b)


s = set()
for i in range(1,100):
    if f(3,i) > 0 and i % 2 == 0:
        s.add(i)
print(len(s))


