def f(filename):
    file = open(filename)
    n = int(file.readline())
    kolichestvo = [0] * 1441
    for i in range(n):
        t_begin, t_end = map(int,file.readline().split())
        for x in range(t_begin,t_end+1):
            kolichestvo[x] += 1
    print(kolichestvo)
    ans2 = max(kolichestvo)
    print("пиковое значение людей", ans2)
    a = []                                          # время начала и время окончания пиков
    for i in range(1,len(kolichestvo)-1):
        if kolichestvo[i-1] != ans2 and kolichestvo[i] == ans2:
            a.append([i])
        if kolichestvo[i] == ans2 and kolichestvo[i+1] != ans2:
            a[-1].append(i)
    return len(a), ans2


print(f("26data/26-130.txt"))
print('___________________')
print(f("130test.txt"))
