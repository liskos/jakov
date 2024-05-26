def f(s):
    while ("91"  in s) or ("92"  in s):
        if "91" in s:
          s = s.replace("91","39",1)
        if "92" in s:
          s = s.replace("92","59",1)
    return s


for i in range(1,100):
  s = "9" + "1" * i + "2" * i
  b = f(s)
  if sum(map(int,b)) > 100:
      print(i,sum(map(int,b)))
