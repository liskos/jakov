def f(s):
    while (">1"  in s) or (">2"  in s) or (">0"  in s):
        if ">1" in s:
          s = s.replace(">1","22>",1)
        if ">2" in s:
          s = s.replace(">2","2>",1)
        if ">0" in s:
          s = s.replace(">0","1>",1)
    return s


for i in range(1,100):
    s = "0" * 39  + "1" * i + "2" * 39
    print(i,sum(map(int,s)))

