def f(s):
    while ("01" in s) or ("02" in s) or ("03" in s):
      s = s.replace("01","2302",1)
      s = s.replace("02","10",1)
      s = s.replace("03","201",1)
    return s


s = "1" * 58 + "2" * 23 + "3" * 15
for i in range(1,1000):
    for o in range(1, 1000):
        for x in range(1, 1000):
          z = "0" + "1" * i + "2" * o + "3" * x
          if f(z) == s:
              print(z.count("2"))
