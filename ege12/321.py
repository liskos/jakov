def f(s):
    while (">2<" not in s):
        s = s.replace(">1",">2",1)
        s = s.replace("12<","1<2",1)
        s = s.replace(">21","1>",1)
        s = s.replace("1<","<2",1)
    return s


for i in range(1,100):
  s = ">2" + "12" * i + "<"
  b = f(s)
  if sum(map(int,b)) == 103:
      print(i)
