for n in range(154026,154043+1):
    div = [d for d in range(1,n+1) if n % d == 0]
    if len(div) == 4:
        print(* div)

print(52)
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)


for n in range(154026,154043+1):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)

#1 3 51343 154029
# 1 2 77017 154034
# 1 31 4969 154039
# 1 3 51347 154041