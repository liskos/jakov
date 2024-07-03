def f(a,b,k):
    if a == b:
        return 1
    if a > b:
        return 0
    k+=1
    return f(a+1,b,k)+f(a*10,b,k)+f(a*10+1,b,k)


v = int("101",2)
z = int("101110",2)
print(f(v,z,0))

