def f(s):
    while ("43" in s) or ("53" in s):
      if "43" in s: s = s.replace("43","33",1)
      else: s = s.replace("53","433",1)
    return s

s = "4" * 23 + "5" * 12 + "53" * 17
print(f(s))
print(f(s).count("3"))