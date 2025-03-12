def f(filename):
    with open(filename) as file:
        m, k, n = map(int, file.readline().split())
        a = [list(map(int, file.readline().split())) for _ in range(n)]

    # Сортируем заявки: сначала по станции посадки, потом по убыванию станции высадки
    a.sort(key=lambda x: (x[0], -x[1]))

    v_poezde = []  # Список станций высадки пассажиров в поезде
    ans1 = 0  # Количество пассажиров, которые смогли доехать
    ans2 = 0  # Количество перегонов, на которых поезд был полон

    for stancia in range(1, m):  # Проходим по всем станциям
        # Высадка пассажиров
        v_poezde = [x for x in v_poezde if x > stancia]

        # Количество свободных мест после высадки
        free_seats = k - len(v_poezde)

        # Собираем пассажиров, которые садятся на этой станции
        new_v = []
        while a and a[0][0] == stancia:
            new_v.append(a.pop(0)[1])

        # Сортируем новых пассажиров по убыванию станции высадки (чтобы дальше едущие садились первыми)
        new_v.sort(reverse=True)

        # Посадка пассажиров
        for destination in new_v:
            if free_seats > 0:
                v_poezde.append(destination)
                free_seats -= 1
                ans1 += 1  # Пассажир смог доехать

        # Если поезд заполнен, увеличиваем счётчик перегонов с полным поездом
        if len(v_poezde) == k:
            ans2 += 1

    return ans1, ans2


print(f("126test.txt"))
print(f("26data/26-126.txt"))
