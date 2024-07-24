def f(a,b,c=0,m=0):
    if a == b and c == 7 and m == 7:
        return 1
    if a > b:
        return 0
    if c == 7:
        return f(a+sum(map(int,str(a))),b,c,m+1)
    return f(a + 2, b, c + 1, m)


print(f(1,70))