for x in range(1,8):
    s1 = f'{x}1{x}'
    s2 = f'{x}3{x}3'
    s = int(s1,16) + int(s2,8)
    print(x,s)