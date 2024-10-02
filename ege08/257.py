import itertools
b = set()
for i,a in enumerate(itertools.product("АЕПСТУХ",repeat=6),1):
    if i > 1000 and "СС" not in "".join(a) and "ТТ" not in "".join(a) and "ПП" not in "".join(a) and "ХХ" not in "".join(a) and "ЕЕ" not in "".join(a) and "УУ" not in "".join(a) and "АА" not in "".join(a):
        b.add(a)
print(len(b))