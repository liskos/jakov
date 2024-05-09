def f(n):
    while '12' in n:
        n = n.replace('12', '4', 1)
    return n

for n in range(1, 15):
    s = "12" * n + (15 - n) * "1"
    if sum(map(int,f(s))) == 48:
        print(n,s)
