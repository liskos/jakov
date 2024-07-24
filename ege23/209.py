
def f(a, b, k=0, memo={}):
    if (a, k) in memo:
        return memo[(a, k)]
    if a == b:
        if k % 2 == 1:
            return 1
    if a > b:
        return 0
    result = f(a + 2, b, k + 1, memo) + f(a * 2, b, k + 1, memo) + f(a ** 2, b, k + 1, memo)
    memo[(a, k)] = result
    return result

print(f(1, 100))