import itertools
b = set()
for i,a in enumerate(itertools.product("ЕЛОПРСТ",repeat=5),1):
    ss = "".join(a).replace("Л","Т").replace("П","Т").replace("Р","Т").replace("С","Т")
    if i % 2 != 0 and a[-1] in "ЕО" and ss.count("Т")< 4:
        b.add(a)

print(len(b))