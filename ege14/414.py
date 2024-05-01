for p in range(2,100):
    for x in range(p):
       for y in range(p):
          for z in range(p):
              n1 = y * p ** 2 + 2 * p ** 1 + y
              n2 = y * p ** 2 + 8 * p ** 1 + 7
              r = 1 * p ** 3 + x * p ** 2 + z * p ** 1 + z
              if (n1 + n2) == r:
                  print(x * p ** 2 + y * p ** 1 + z)

