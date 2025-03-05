def f(filename):
    file = open(filename)
    n =int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    b = [[0, 0]]
    for i in range(len(a)):
        t_end = b[-1][1]  # время окончания
        dopushen = [r for r in a if r[0] >= t_end] # которые можно выбрать
        if not dopushen:
            break
        vibor = min(dopushen, key=lambda x:x[1])# выбираем то которое закончится раньше
        b.append(vibor)
    t_end = b[-2][1]
    dopushen = [r for r in a if r[0] >= t_end]
    ans2 = max(dopushen,key= lambda x:x[1])
    return len(b)-1,ans2[1]


print(f("128test.txt"))
print(f("26data/26-128.txt"))