def f(filename):
    file = open(filename)
    v,k,n = map(int,file.readline().split())
    p = [int(file.readline()) for _ in range(n)]
    b = [v] * k
    p = sorted(p,reverse=True)
    otv = []

    print(b)
    j = -1 #текущий диск
    for i in range(n): #номер архива
        if max(b) < p[i]: #проверка что в архив помещается на одним из дисков
            otv.append(p[i])
            continue
        j += 1
        j %= k
        while b[j] < p[i]:
            j += 1
            j = j % k
        b[j] -= p[i]
    return sum(otv),len(otv)

    print(otv)
    return sum(otv),len(otv)
print(f("56test.txt"))

print(f("26data/26-56.txt"))