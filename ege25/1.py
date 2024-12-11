for n in range(126849, 126871+1):
  divs = [d for d in range(1, n+1) if n % d == 0]
  if len(divs) == 4:
    print( *divs )



# 1 3 42283 126849
# 1 47 2699 126853
# 1 5 25373 126865
# 1 293 433 126869
