
def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 2 == 0:
        if f(n//2) == "бесконечность":
            return "бесконечность"
        return 1 + f(n // 2)
    if n > 1 and n % 2 != 0:
        return "бесконечность"

for i in range(1,100000):
    if f(i) == 16:
        print(i,f(i))


