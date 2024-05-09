def s(s):
    while '23' in s:
        s = s.replace('23', '7', 1)
    return s

def f(t):
    total_sum = 82
    min_twos = total_sum // 2
    for twos_count in range(min_twos, total_sum + 1):
        threes_count = (total_sum - 2 * twos_count) // 3
        s = '22' * twos_count + '33' * threes_count
        result = s(s)
        if sum(map(int, result)) == total_sum:
            return twos_count

min_twos = s()
print( min_twos)