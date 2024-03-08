def f(n):
    s = sorted(list(str(n)))
    if s[0] != '0':
        return int(s[2] + s[1]) - int(s[0] + s[1])
    elif s[1] != '0':
        return int(s[2] + s[1]) - int(s[1] + s[0])
    else:
        return 0


print(f(351))
k = 0
for i in range(100,1000):
    if f(i) == 35:
        k += 1
print(k)