def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for x in range(n)]
    a = sorted(a,reverse=True)
    v = [] # добавляем массив
    while a:
        v.append(a[0])
        a.pop(0)
        a = [x for x in a if x <= v[-1] - 9]
    return len(v),v[-1]

print(f("26test.txt"))
print(*f("26_21910.txt"))