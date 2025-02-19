def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int, file.readline().split())) for _ in range(n)]  # Считываем n строк и преобразуем в список списков
    print(a)
    for x in range(len(a)):
        


print(f("159test.txt"))