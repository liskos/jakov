for i in range(81234, 81299):
    ds = set() # Чётные делители
    for d in range(1, int(i**0.5)+1):
        if i % d == 0:
            # Проверяем чётность делителей
            if d % 2 == 0:
                ds.add(d)
            if (i//d) % 2 == 0:
                ds.add(i//d)
        # Если кол-во превышает 4, то пропускаем
        if len(ds) > 4:
            break
    if len(ds) == 4:
        print(sorted(ds))