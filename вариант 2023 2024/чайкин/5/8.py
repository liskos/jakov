import itertools
for i,a in enumerate(itertools.product("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",repeat=8),0):
    if "".join(a) == "РЕКУРСИЯ":
        print(i)
