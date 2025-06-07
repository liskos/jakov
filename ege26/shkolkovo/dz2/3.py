def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    b = sorted([x for x in a if x > 153])
    skid = b[:int(len(b)/4)]
    print(skid)
    otv1 = sum(a) - sum(skid) * 0.4

    otv2 = [x for x in a if x <= 153]
    otv2 = sum(otv2) / len(otv2)

    return int(otv1+0.999),int(otv2)




print(f("26_3test.txt"))
print(*f("files/26_23__1kuc9.txt"))