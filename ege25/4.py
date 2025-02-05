for n in range(209834,209857+1):
    div = [d for d in range(1,n+1) if n % d == 0]
    if len(div) == 4:
        print(* div)

print(52)

def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(209834,209858):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)


#1 2 104917 209834
# 1 223 941 209843
# 1 5 41969 209845
# 1 173 1213 209849