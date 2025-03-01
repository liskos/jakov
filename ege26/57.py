def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split()) #n = кол-во m - длина
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    sv = 0 #количество сварок
    while sum(a) >= m:     #пока сумма кусков  больше или равна нужного
        s = [] #выбранные отрезки
        for i in range(len(a)):
            if sum(s) >= m:
                break
            else:
                s.append(a[i])
        a = a[i-1:]
        s = s[:-1]
        ost = m - sum(s) #длина последнего куска должна быть не менее ost
        r = min([x for x in a if x >= ost]) # последний выбранный кусок с учетом минимизации остатков
        s.append(r)
        a.remove(r)
        sv += len(s)-1
        if sum(s) > m:
            a.append(sum(s)-m)

    return sv,len(a)

print(f("57test.txt"))
print(f("26data/26-57.txt"))