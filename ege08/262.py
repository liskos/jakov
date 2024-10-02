import itertools
b = set()
for i,a in enumerate(itertools.product("АЕЖЙМУ",repeat=5),1):
    if i % 2 == 0 and "УУ" not in "".join(a) and "ЖЖ" not in "".join(a) and "ЕЕ" not in "".join(a) and "ММ" not in "".join(a) and "АА" not in "".join(a) and "ЙЙ" not in "".join(a):
        b.add(a)
print(len(b),b)