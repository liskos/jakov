def f(filename):
    file = open(filename)
    n = int(file.readline())
    s = [int(file.readline()) for _ in range(n)]
    s = sorted(s)
    money = 100000
    count = 0
    for i in range(len(s)-1):
        price = s[i] if (count + 1) % 6 != 0 else s[i] // 2
        if money >= price:
            money -= price
            count += 1
        else:
            break
    return count,money


print(f("109test.txt"))
print(f("26data/26-109.txt"))