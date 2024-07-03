def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 33:
        return 0
    return f(a+2,b)+f(a,b)

print(f(2,14)*f(14,45))


