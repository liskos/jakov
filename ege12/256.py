def f(s):
    while ("333" in s) or ("111" in s):
        s = s.replace("333","11",1)
        s = s.replace("111","3",1)
    return s


for i in range(100,160):
  s = "1" * i
  b = f(s)
  if b.count("1") >= 2:
    print(s.count("1"),sum(map(int,b)))

