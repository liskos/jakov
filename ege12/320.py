def f(s):
    while ("11" in s) or ("22" in s) or ("13" in s) or ("23" in s):
        s = s.replace("11","2",1)
        s = s.replace("22","1",1)
        s = s.replace("13","2",1)
        s = s.replace("23","1",1)
    return s


for i in range(1,100):
  s = "1" * 33 + "3" * i + "2" * 33 + "3" * i
  b = f(s)
  print(b,"!!!",s,s.count("3"))