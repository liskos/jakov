a = set()
for x in range(0,8):
    for y in range(0,8):
        s = int(f"36{x}53",8) - int(f"4{y}{y}3",8)
        if s> 0:
            a.add(s)
print(min(a))