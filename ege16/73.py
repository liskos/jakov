
def f(n):
    if n < 50:
        return n
    if n > 49:
        return 2 * g(50 - n//2)


def g(j):
    if j > 40:
        return 10
    if j < 41:
        return 30 + f(j + 600 // j)





print(f(80))

