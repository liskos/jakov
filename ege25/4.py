for n in range(209834,209857+1):
    div = [d for d in range(1,n+1) if n % d == 0]
    if len(div) == 4:
        print(* div)