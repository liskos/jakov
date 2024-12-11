for n in range(102714,102725+1):
    div = [d for d in range(1,n+1) if n % d == 0]
    if len(div) == 4:
        print(* div)