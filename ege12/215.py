def f(s):
    while "111" in s:
            s = s.replace('111',"2",1)
            s = s.replace('222','1',1)
    return s

r = "2"
min = r.count("1") + r.count("2")
maxx = min * 3

for i in range(min, maxx + 1):
    s = "1" * i
    output_string = f(s)
    if output_string == r:
        print(f"{i}")
        break