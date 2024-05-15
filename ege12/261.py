def f(s):
    while ("aa" in s) or ("bb" in s) or ("ab" in s) :
      s = s.replace("aa","b",1)
      s = s.replace("bb","a",1)
      s = s.replace("ab","ba",1)
    return s

s = "ab" * 52
print(f(s))
