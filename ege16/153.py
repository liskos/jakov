import functools
@functools.lru_cache(None)
def f(n):
    if n < 10:
        return 0
    return f(n//10) + (n//10%10)-(n%10)


k = 0
for i in range(1,10**4+1):
    if f(i) == 9:
        k+=1
        print(i)
print(k)

