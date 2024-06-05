import functools
@functools.lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 3 == 0:
        return 2 * f(n-1)+f(n-2)
    else:
        return 3 * f(n-2)+f(n-1)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

a = []
for i in range(1,36):
    b = str(f(i))
    if (is_prime(sum(map(int,b)))) == True:
        a.append(i)
print(len(a))
