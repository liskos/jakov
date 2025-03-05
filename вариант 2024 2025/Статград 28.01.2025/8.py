import itertools
k = 0
for a in itertools.product("0123456789abcde",repeat=14):
    if a[0] != "0":
        print(a)
        if int("".join(a),15) <= 855000000 and 14 - len(set(a)) == 6:
            k += 1

print(k)