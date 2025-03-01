from tkinter.messagebox import RETRY


def f(filename, k):
    file = open(filename)
    n = int(file.readline())
    a = [[False]*8 for _ in range(k)]
    for _ in range(n):
        str, n_mark = map(int, file.readline().split())
        a[str-1][n_mark - 1] = True
    print(a)
    b = [x.count(False) for x in a]
    m = max(b)
    c = [i for i in range(k) if b[i] == m]
    print(m , c)
    return sum(b), max(c) + 1

print(f("77test.txt", 3))
print(*f("26data/26-77.txt", 30))