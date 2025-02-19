def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [0]*100
    for _ in range(n):
        a[int(file.readline())] += 1
    print(a)
    k = 0
    for i in range(1,50):
        k+=min(a[i],a[100-i])
    k += a[50] // 2
    return k

print(f("26test.txt"))
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(f("26data/26-j1.txt"))