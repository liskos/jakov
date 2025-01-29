from lib2to3.btm_utils import rec_test


def delitel(n):
  a = set()
  for i in range(1,int(n**0.5)+1):
    if n % i == 0:
      a.add(i)
      a.add(n//i)
  return sorted(a)


for n in range(126849, 126871+1):
  divs = delitel(n)
  if len(divs) == 4:
    print( *divs )



# 1 3 42283 126849
# 1 47 2699 126853
# 1 5 25373 126865
# 1 293 433 126869
