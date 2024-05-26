def f(s):
    while ("01" in s) or ("02" in s) or ("03" in s):
      s = s.replace("01","2302",1)
      s = s.replace("02","10",1)
      s = s.replace("03","201",1)
    return s

s = "0" + "1" * 60 + "2" * 22 + "3" * 17
res = f(s)
print(res.count("1"))

