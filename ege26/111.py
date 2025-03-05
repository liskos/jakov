def f(filename):
    file = open(filename)
    k = int(file.readline())
    n = int(file.readline())
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    a = sorted(a, key=lambda x: x[0])  # Сортируем по времени сдачи

    v = []  # Пары (время_освобождения, номер_ячейки)
    otv1 = 0
    k1 = 0

    for i in range(n):
        # Освобождаем ячейки, если можно
        v.sort()
        if len(v) > 0 and v[0][0] < a[i][0]:
            otv1 += 1
            v.pop(0)  # Освобождаем самую раннюю ячейку
            v.append((a[i][1], v[0][1]))  # Сажаем нового пассажира в эту же ячейку
        elif k1 < k:
            otv1 += 1
            k1 += 1
            v.append((a[i][1], k1))  # Сажаем нового пассажира в новую ячейку

    # Номер последней занятой ячейки (минимальный из последних)
    last_cell = min([x[1] for x in v])

    return otv1, last_cell


print(f("111test.txt"))
# print(f("26data/26-111.txt"))
