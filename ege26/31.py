def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    b = [x for x in a if x > 100]
    b = sorted(b)
    k = int(len(b)//2)
    skid = b[:k]
    if sum(skid)*0.9 != int(sum(skid)*0.9):
        skids = sum(skid)*0.9 + 1
    else:
        skids = sum(skid)
    a = [x for x in a if not skid.count(x)]
    return int(sum(a)+skids),max(skid)


print(f("31test.txt"))
print("!!!!!!!!!!!!!!!!!!!")
print(f("26data/26-s1.txt"))