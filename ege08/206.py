import itertools
b = set()
for a in itertools.product("ЯСНОВИДЕЦ",repeat=5):
    ss = "".join(a).replace("Я","Е").replace("О","Е").replace("И","Е")
    ss = ss.replace("С","Ц").replace("Н","Ц").replace("В","Ц").replace("Д","Ц")
    if a[0] in "СНВДЦ" and a[-1] in "ЯОЕИ":
        if a.count(a[0]) == 1 and a.count(a[-1]) == 1 and a[0] not in "ЯОА":
            b.add(a)
print(len(b),b)


