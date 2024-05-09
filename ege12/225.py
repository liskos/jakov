def f(n):
    while '12' in n:
        n = n.replace('12', '4', 1)
    return n

def d(f):
    f = (original_sum - 15) // (4-2) + 1
    return f

original_sum = 48
min_twos = d(original_sum)
print(min_twos)
