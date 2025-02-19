def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    skidka = a[:k]
    bezskidki = a[k:]
    print(skidka,bezskidki)

    return max(bezskidki),sum(skidka) * 0.2
    # p = 0
    # b = []
    # for x in a:
    #     if p < k:
    #         p += 1
    #         a.remove(x)
    #         b.append(x)
    # print(a, b)
    # b = sum(b) * 0.2
    #
    # return max(a),b


print(f("21test.txt"))
print(f("26data/26-k1.txt"))