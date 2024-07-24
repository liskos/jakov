import functools
@functools.lru_cache(None)
def f(x,y,z=17,w=27):
    if x == z:
        return 1
    if y == w:
        return 1
    if y > w:
        return 0
    if x > z:
        return 0
    return f(x+1,y,z,w)+f(x+2,y,z,w)+f(x,y+3,z,w)


print(f(1,0))