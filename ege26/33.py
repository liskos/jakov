def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    b = [x for x in a if x > 200]
    b = sorted(b)
    k = int(len(b)//2)
    skid = b[:k]
    if sum(skid)*0.7 != int(sum(skid)*0.7):
        skids = sum(skid)*0.7 + 1
    else:
        skids = sum(skid)
    a = [x for x in a if not skid.count(x)]
    return int(sum(a)+skids),max(skid)


print(f("33test.txt"))
print("!!!!!!!!!!")
print(f("26data/26-s1.txt"))