def f(s):
    while ("01" in s) or ("02" in s) or ("03" in s):
      s = s.replace("01","302",1)
      s = s.replace("02","3103",1)
      s = s.replace("03","20",1)
    return s


s = "0" + "1" * 28 + "2" * 34 + "3" * 45

b = f(s)
print(b.count("1"),b)

