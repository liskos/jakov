def f(s):
    while "111" in s:
        s = s.replace("111","2",1)
        s = s.replace("2222","333",1)
        s = s.replace("33","1",1)
    return s

for i in range(90,160):
  s = "1" * i
  b = f(s)
  if b.count("1") >= 4:
    print(len(s),b.count("1"))
