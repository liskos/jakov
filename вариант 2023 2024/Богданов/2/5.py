def f(n):
    n = bin(n)[2:]
    if len(n) % 2 != 0:
        if n[len(n)//2] == '0':
            n = n[:len(n) // 2] + '1' + n[len(n) // 2 + 1:]
        else:
            n = n[:len(n) // 2] + '0' + n[len(n) // 2 + 1:]
    else:
        s1 = n[:len(n)//2 - 1]
        s2 = n[len(n)//2-1:len(n)//2 + 1]
        s3 = n[len(n)//2+1:]
        s4 = ''
        for i in s2:
            if i == '1':
                s4 += '0'
            else:
                s4 += '1'
        n = s1 + s4 + s3
    return int(n,2)

for n in range(5,1000):
    if f(n) > 100 and f(n) < n:
        print(n)
        break
