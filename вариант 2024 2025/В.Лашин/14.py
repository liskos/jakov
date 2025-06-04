def chr(n):
  #  n = abs(n)
    s = ""
    t = "0123"
    while n > 0:
        s = t[n%4] + s
        n //= 4
    return s

for x in range(1,263170):
    s = 4 ** 8 + 4 ** 5 - x
    b = chr(s)
    if b.count("0") == 8:
        print(x,int(b,4))
