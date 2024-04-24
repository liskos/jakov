def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

import sys
sys.setrecursionlimit(2500)
print(f(2024)/f(2022))