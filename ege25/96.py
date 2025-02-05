def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


for n in range(81234,134689+1):
    divs = delitel(n)
    if len(divs) == 5:
        print(min(divs),max(divs),divs)


#17 4913
#19 6859