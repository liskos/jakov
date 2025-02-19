def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    otlich = a[:k]
    horoshist = a[k:k*2]
    return sum(horoshist)/len(horoshist),sum(otlich)/len(otlich)


print(f("24test.txt"))
print("_____________________")
print(f("26data/26-k4.txt"))