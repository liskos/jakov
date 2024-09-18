aa = []
for x in "abcd":
    for y in "9abcd":
        if int(x, 14) > int(y, 14):
            a = f"7{x}37{y}"
            b = f"9{y}63"
            c = "15148"
            s = int(a,14) + int(b,int(x,14)) - int(c,int(y,14))
            aa.append(s)
            if s == 316323:
                print(x, y, s//(int(x, 14) + int(y,14)))
print(max(aa))
