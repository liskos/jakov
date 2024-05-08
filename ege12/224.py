count = set()
for i in range(33):
    s = "1" + "1" * i
    while "21" in s:
        s = s.replace("21", "6", 1)
    count.add(s.count("1"))

print(len(count))