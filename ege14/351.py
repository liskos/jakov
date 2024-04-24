for x in '123456789abc':
  if int(x + '1418', 13) + int('1' + x + '037', 14) == int('2' + x + '209', 19):
    print(int('2' + x + '209', 19))
    break