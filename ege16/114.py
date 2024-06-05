
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
def f(n):
    if n == 1:
        return 0
    if n > 0:
        return 7 * (n-1)+f(n-1)

a = []
for i in range(2,201):
    if is_prime(f(i)) == True:
        a.append(i)
print(len(a))


