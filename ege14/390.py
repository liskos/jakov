def tr(n):
    t = '0123456789ab'
    s = ''
    while n > 0:
        s = t[n % 12] + s
        n = n // 12
    return s
for x in "0123456789abcdef":
    for y in "01234567":
     s1 = f"57a{x}9"
     s2 = f"54{y}"
     s = int(s1, 16) * int(s2, 8)
     if tr(sum(map(int,str(s))))== '40':
            print(x,s)
print(int('127787268',12))


