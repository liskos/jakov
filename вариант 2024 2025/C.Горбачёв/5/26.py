def f(filename):
    file = open(filename)
    n,m,k = map(int,file.readline().split())
    a = [m]*(k+1)
    print(f"кол-во рядов - {m}",f"количество мест в ряду - {k}")
    for i in range(n):
        row,column = map(int,file.readline().split())
        a[column] = min(a[column],row-1)
    print(a)
    mn = 0 # искомый ряд
    z = 0  # наибольший номер места
    for i in range(1,k+1-3):
        if min(a[i:i+4]) >= mn:
            mn = min(a[i:i+4])
            z = i+3
    return mn, z

print(f("26test.txt"))
print(*f("26(3).txt"))







