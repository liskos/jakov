def f(n):
    if n ** 0.5 > 0:
        return n ** 0.5
    if (n ** 0.5).is_integer == False:
        return f(n+1)+1


print(f(4850 + f(5000)))