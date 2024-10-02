import itertools
b = set()
for i,a in enumerate(itertools.product("АПРСУ",repeat=5),1):
    if a[0] == "У" and "АА" not in "".join(a):
        print(a,i)
