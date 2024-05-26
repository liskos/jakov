def f(s):
    while ("01" in s) or ("02" in s) or ("03" in s):
      s = s.replace("01","30",1)
      s = s.replace("02","3103",1)
      s = s.replace("03","1201",1)
    return s


s = "0" + "1" * 7 + "2" * 19 + "3" * 21

b = f(s)
print(b.count("1"),b.count("2"),b.count("3"))

