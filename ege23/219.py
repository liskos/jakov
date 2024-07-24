from functools import cache
@cache
def f(a,b,k=0,v=0):
    if k > 200:
        return 10**20
    if a == b and k == 30:
        return v
    if a > b:
        return 10**20
    if k > 30:
        return min(f(a*2,b,k,v+1),f(a*3,b,k,v+1))
    return min(f(a+1,b,k+1,v+1),f(a*2,b,k,v+1),f(a*3,b,k,v+1))


print(f(1,9217))