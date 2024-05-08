count = set()
for i in range(33):
    s = "1" + "1" * i
    while "111" in s:
        s = s.replace("111", "33", 1)
        s = s.replace("333", "1")
    count.add(s.count("1"))

print(len(count))