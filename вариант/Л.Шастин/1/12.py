def f(s):
    while "55555" in s:
        s = s.replace('55555',"88",1)
        s = s.replace('888','55',1)
    return s


a = []
for i in range(51,1000):
    s = '5' * i
    if f(s).count("5")==6:
        print(i)
        break